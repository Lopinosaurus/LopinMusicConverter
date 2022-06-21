# bot.py
# region Library
import os

import discord
from dotenv import load_dotenv
import json
#endregion

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected !')
    await client.change_presence(activity = discord.Game(name="You're a fucking nerd"))

@client.event
async def on_message(message):
    # Ignore self messages
    if message.author == client.user:
        return

@client.event
async def on_member_update(before, after):
    return 
