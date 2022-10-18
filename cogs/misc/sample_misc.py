import discord
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def misc(self, ctx):
        await ctx.send("I am a misc command.")


def setup(client):
    client.add_cog(Misc(client))
