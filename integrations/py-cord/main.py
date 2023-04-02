# This is a testing module which interfaces with `py-cord`. You will need to
# have an environment variable called 'COGWATCH_BOT_TOKEN' set in order for this
# to run. Additionally, you will need to have the `py-cord` package installed.

import asyncio
import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from cogwatch import Watcher, watch

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True


class ExampleBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='.', intents=intents)

    @watch(path='integrations/py-cord/commands', preload=True)
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
