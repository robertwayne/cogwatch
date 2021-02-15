import asyncio
import os

from discord.ext import commands

from cogwatch import watch

# This let's us easily load our bot token from a .env
# file in the root directory so it is never exposed.
from dotenv import load_dotenv

load_dotenv()


class ExampleBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

    @watch(path="commands", debug=False)
    async def on_ready(self):
        print("Bot ready.")

    async def on_message(self, message):
        if message.author.bot:
            return

        await self.process_commands(message)


async def main():
    client = ExampleBot()
    await client.start(os.getenv("COGWATCH_BOT_TOKEN"))


# This function is specifically for running from a poetry script.
# You do not need this in your own bot, you can remove these 2 lines.
def __poetry_run():
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
