import asyncio
import logging
import sys
from functools import wraps
from pathlib import Path

from discord.ext import commands
from watchgod import Change, awatch

logger = logging.getLogger('cogwatch')
logger.addHandler(logging.NullHandler())


class Watcher:
    """The core cogwatch class -- responsible for starting up watchers and managing cogs.

    Attributes
        :client: A discord Bot client.
        :cogs_path: Root name of the cogs directory; cogwatch will only watch within this directory -- recursively.
        :debug: Whether to run the bot only when the debug flag is True. Defaults to True.
        :loop: Custom event loop. If not specified, will use the current running event loop.
        :default_logger: Whether to use the default logger (to sys.stdout) or not. Defaults to True.
        :preload: Whether to detect and load all found cogs on startup. Defaults to False.
    """
    def __init__(self, client: commands.Bot, cogs_path: str = 'commands', debug: bool = True,
                 loop: asyncio.BaseEventLoop = None, default_logger: bool = True, preload: bool = False):
        self.client = client
        self.cogs_path = cogs_path
        self.debug = debug
        self.loop = loop
        self.default_logger = default_logger
        self.preload = preload

        if default_logger:
            _default = logging.getLogger(__name__)
            _default.setLevel(logging.INFO)
            _default_handler = logging.StreamHandler(sys.stdout)
            _default_handler.setFormatter(logging.Formatter('[%(name)s] %(message)s'))
            _default.addHandler(_default_handler)

    @staticmethod
    def get_cog_name(path: str) -> str:
        """Returns the cog file name without .py appended to it."""
        return path.split('\\')[-1:][0][:-3]

    def get_dotted_cog_path(self, path: str) -> str:
        """Returns the full dotted path that discord.py uses to load cog files."""
        full_dir = Path(path).parents[0]
        tokens = str(full_dir).split('\\')
        root_index = tokens.index(self.cogs_path)

        return '.'.join([token for token in tokens[root_index:]])

    async def _start(self):
        """Starts a watcher, monitoring for any file changes and dispatching event-related methods appropriatly."""
        logger.info('Watching for file changes...')

        while True:
            async for changes in awatch(Path.cwd() / self.cogs_path):
                reverse_ordered_changes = sorted(changes, reverse=True)

                for change in reverse_ordered_changes:
                    change_type = change[0]
                    change_path = change[1]

                    filename = self.get_cog_name(change_path)

                    new_dir = self.get_dotted_cog_path(change_path)
                    cog_dir = f'{new_dir}.{filename.lower()}' if new_dir else f'{self.cogs_path}.{filename.lower()}'

                    if change_type == Change.deleted:
                        await self.unload(cog_dir)
                    elif change_type == Change.added:
                        await self.load(cog_dir)
                    elif change_type == Change.modified and change_type != (Change.added or Change.deleted):
                        await self.reload(cog_dir)

            await asyncio.sleep(1)

    def check_debug(self):
        """Determines if the watcher should be added to the event loop based on debug flags."""
        if self.debug:
            if __debug__:
                return True
            else:
                return False
        else:
            return True

    async def start(self):
        """Checks for a user-specified event loop to start on, otherwise uses current running loop."""
        if self.preload:
            await self._preload()

        if self.check_debug():
            if self.loop is None:
                self.loop = asyncio.get_event_loop()
            self.loop.create_task(self._start())

    async def load(self, cog_dir: str):
        """Loads a cog file into the client."""
        try:
            self.client.load_extension(cog_dir)
        except Exception as exc:
            self.cog_error(exc)
        else:
            logger.info(f'Cog Loaded: {cog_dir}')

    async def unload(self, cog_dir: str):
        """Unloads a cog file into the client."""
        try:
            self.client.unload_extension(cog_dir)
        except Exception as exc:
            self.cog_error(exc)
        else:
            logger.info(f'Cog Unloaded: {cog_dir}')

    async def reload(self, cog_dir: str):
        """Attempts to atomically reload the file into the client."""
        try:
            self.client.reload_extension(cog_dir)
        except Exception as exc:
            self.cog_error(exc)
        else:
            logger.info(f'Cog Reloaded: {cog_dir}')

    @staticmethod
    def cog_error(exc: Exception):
        """Logs exceptions. TODO: Need thorough exception handling."""
        if isinstance(exc, (commands.ExtensionError, SyntaxError)):
            logger.exception(exc)

    async def _preload(self):
        logger.info('Preloading...')
        for cog in {(file.stem, file) for file in Path(Path.cwd() / self.cogs_path).rglob('*.py')}:
            new_dir = self.get_dotted_cog_path(cog[1])
            await self.load('.'.join([new_dir, cog[0]]))


def watch(**kwargs):
    """Instantiates a watcher by hooking into a Bot client methods' `self` attribute."""
    def decorator(function):
        @wraps(function)
        async def wrapper(client):
            cw = Watcher(client, **kwargs)
            await cw.start()
            retval = await function(client)
            return retval
        return wrapper
    return decorator
