import asyncio

from discord.ext import commands

from cogwatch import watch


class ExampleBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!')

    @watch(cogs_path='commands', debug=False, loop=None, default_logger=True)
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
