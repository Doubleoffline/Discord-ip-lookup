import requests
import discord
from discord.ext import commands

import discord
from discord.ext import commands
import requests

class iplookup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("iplookup.py is ready")

    @commands.command()
    async def iplookup(self, ctx, ip: str):
        try:
            response = requests.get(f"https://ipinfo.io/{ip}/json")
            data = response.json()

            embed = discord.Embed(title=f"IP Lookup for {ip}", url=f"https://maps.google.com/?q={data['loc']}", color=0x0099ff)
            embed.add_field(name="IP Address", value=data["ip"])
            embed.add_field(name="Location", value=f"{data['city']}, {data['region']}, {data['country']}")
            embed.add_field(name="Organization", value=data["org"])
            embed.add_field(name="Time Zone", value=data["timezone"])
            latitude, longitude = map(float, data["loc"].split(','))
            embed.add_field(name="Latitude", value=latitude)
            embed.add_field(name="Longitude", value=longitude)

            await ctx.send(embed=embed)
        except:
            await ctx.send("An error occurred while trying to lookup the IP address.")

async def setup(client):
    await client.add_cog(iplookup(client))


