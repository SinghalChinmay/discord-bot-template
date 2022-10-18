import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Loading the tokens
load_dotenv()
TOKEN = os.getenv("TOKEN")
MONGO = os.getenv("MONGO")

intents = discord.Intents.default()
client = commands.Bot(command_prefix=commands.when_mentioned_or("."), intents=intents)
client.remove_command("help")  # removing the default help command for custom one.


@client.command()
@commands.is_owner()  # Owner only command
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} extension")


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded {extension} extension")


for folder in os.listdir("./cogs"):
    if (
        os.path.isdir("./cogs/" + folder) and folder.endswith("_") is False
    ):  # Searches for folders in cogs folder
        for file in os.listdir("./cogs/" + folder):
            if file.endswith(".py"):  # Checks for python files in the folder
                client.load_extension(
                    f"cogs.{folder}.{file[:-3]}"
                )  # Loads the extension


@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)}ms")


client.run(TOKEN)
