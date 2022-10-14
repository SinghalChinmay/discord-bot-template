import discord
from os import getenv
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = getenv("TOKEN")

intents = discord.Intents.default()
client = commands.Bot(command_prefix=commands.when_mentioned_or("."), intents=intents)

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

client.run(TOKEN)