[![PyPI version](https://badge.fury.io/py/cogwatch.svg)](https://badge.fury.io/py/cogwatch)

# cogwatch

*Automatic hot-reloading for your discord.py command files.*

`cogwatch` is a utility that you can plug into your `discord.py` bot that will watch your command files directory *(cogs)* 
and automatically reload them as you modify or move them around in real-time. No more manually reloading commands with 
other commands, or *(worse yet)* restarting your bot, every time you edit that embed!

### Getting Started
You can install the library with `pip install cogwatch`.

Import the `@watch()` decorator and apply it to your `on_ready` method and let the magic take effect.

```python
import asyncio
from discord.ext import commands
from cogwatch import watch


class ExampleBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!')

    @watch()
    async def on_ready(self):
        print('Bot ready.')

    async def on_message(self, message):
        if message.author.bot:
            return

        await self.process_commands(message)


async def main():
    bot = ExampleBot()
    await bot.start('TOKEN_HERE')

if __name__ == '__main__':
    asyncio.run(main())
```

**NOTE:** `cogwatch` will only run if the **\_\_debug\_\_** flag is set on Python. You can read more about that 
[here](https://docs.python.org/3/library/constants.html). In short, unless you run Python with the *-O* flag from
your command line, **\_\_debug\_\_** will be **True**. If you just want to bypass this feature, pass in `debug=False` and
it won't matter if the flag is enabled or not. *This is a development tool. You should not run it on production.*

### Configuration
You can pass any of these values to the decorator:

**cogs_path='commands'**: Root name of the cogs directory; cogwatch will only watch within this directory -- recursively.

**debug=True**: Whether to run the bot only wheen the Python **\_\_debug\_\_** flag is True. Defaults to True.

**loop=None**: Custom event loop. Defaults to the current running event loop.

**default_logger=True**: Whether to use the default logger *(to sys.stdout)* or not. Defaults to True.

**preload=False**: Whether to detect and load all found cogs on startup. Defaults to False.

### Logging
By default the utility has a logger configured so users can get output to the console. You can disable this by
passing in `default_logger=False`. If you want to hook into the logger -- for example, to pipe your output to another
terminal or `tail` a file -- you can set up a custom logger like so:

```python
import logging
import sys

watch_log = logging.getLogger('cogwatch')
watch_log.setLevel(logging.INFO)
watch_handler = logging.StreamHandler(sys.stdout)
watch_handler.setFormatter(logging.Formatter('[%(name)s] %(message)s'))
watch_log.addHandler(watch_handler)
```
