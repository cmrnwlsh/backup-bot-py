import os
from os.path import join
from zipfile import ZipFile, ZIP_DEFLATED
import json
import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
path = os.path.dirname(__file__)
world_path = join(path, 'worlds_local')
token = json.load(open(join(path, 'config.json')))['token']


@tree.command()
async def world(interaction):
    """download the current world"""
    await interaction.response.defer(ephemeral=False, thinking=True)

    with ZipFile('world.zip', 'w', compression=ZIP_DEFLATED, compresslevel=9) as world:
        world.write(join(world_path, 'Dedicated.db'), 'Dedicated.db')
        world.write(join(world_path, 'Dedicated.fwl'), 'Dedicated.fwl')
        world.close()

    await interaction.followup.send(file=discord.File(
        join(path, world.filename)
    ))


@client.event
async def on_ready():
    await tree.sync()


client.run(token)
