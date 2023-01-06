from discord.ext import commands

from cogwatch import Watcher

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot ready.')

    watcher = Watcher(client, path='commands', preload=True, debug=False)
    await watcher.start()


client.run('YOUR_TOKEN_GOES_HERE')
