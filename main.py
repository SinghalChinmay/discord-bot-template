import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Loading the tokens
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
client = commands.Bot(command_prefix=commands.when_mentioned_or("."), intents=intents)
client.remove_command("help")  # removing the default help command for custom one.


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} extension")


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded {extension} extension")


for folder in os.listdir("./cogs"):
    if os.path.isdir("./cogs/" + folder) and folder.endswith("_") is False:
        for file in os.listdir("./cogs/" + folder):
            if file.endswith(".py"):
                client.load_extension(f"cogs.{folder}.{file[:-3]}")


@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)}ms")


client.run(TOKEN)
