import os
import json
import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
path = os.path.dirname(__file__)
token = json.load(open(os.path.join(path, 'config.json')))['token']


@tree.command()
async def world(interaction):
    """download the current world"""
    await interaction.response.send_message(files=[
        discord.File(os.path.join(path, 'worlds_local/Dedicated.db')),
        discord.File(os.path.join(path, 'worlds_local/Dedicated.fwl'))
    ])


@client.event
async def on_ready():
    await tree.sync()


client.run(token)
