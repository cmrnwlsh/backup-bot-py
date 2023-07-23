import json
import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
token = json.load(open('config.json'))['token']


@tree.command()
async def world(interaction):
    """download the current world"""
    await interaction.response.send_message(files=[
        discord.File('./worlds_local/Dedicated.db'),
        discord.File('./worlds_local/Dedicated.fwl')
    ])


@client.event
async def on_ready():
    await tree.sync()


client.run(token)
