import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fun(self, ctx):
        await ctx.send("I am a fun command.")


def setup(client):
    client.add_cog(Fun(client))
