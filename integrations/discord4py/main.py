# This is a testing module which interfaces with
# `discord.py-message-components`. You will need to have an environment variable
# called 'COGWATCH_BOT_TOKEN' set in order for this to run. Additionally, you
# will need to have the `discord.py-message-components` package installed.

import asyncio
import logging
import os

from discord.ext import commands
from dotenv import load_dotenv

from cogwatch import Watcher, watch

load_dotenv()


class ExampleBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='.')

    @watch(path='integrations/discord4py/commands', preload=True)
    async def on_ready(self):
        logging.info('Bot ready.')

    async def on_message(self, message):
        logging.info(message)

        if message.author.bot:
            return

        await self.process_commands(message)


async def main():
    client = ExampleBot()
    await client.start(os.getenv('COGWATCH_BOT_TOKEN'))


def __poetry_run():
    asyncio.run(main())


if __name__ == '__main__':
    asyncio.run(main())
