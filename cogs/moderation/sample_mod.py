import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mod(self, ctx):
        await ctx.send("I am a moderation command.")


def setup(client):
    client.add_cog(Moderation(client))
