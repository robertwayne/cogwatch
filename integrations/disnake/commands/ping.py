from disnake.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply('Pong!')


def setup(client):
    client.add_cog(Ping(client))
