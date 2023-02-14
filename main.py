import discord
from discord.ext import commands, tasks
import os
import asyncio


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
stauts = "Double Bot"


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(stauts))


@client.event
async def on_ready():
    print(f"The login in {client.user} has beed done")
    change_status.start()


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with client:
        await load()
        await client.start("bot token")

asyncio.run(main())
