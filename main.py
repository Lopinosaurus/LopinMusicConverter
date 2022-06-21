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
    await client.change_presence(activity = discord.Game(name="You are a fucking nerd"))

@client.event
async def on_message(message):
    # Ignore self messages
    if message.author == client.user:
        return

    if message.content.lower().startwith('$start'):
        players = open('players.json', 'r+', encoding="utf-8")
        json.load(players)
        players_list = players['players']

    if message.content.lower().startswith('$ut'):
        players = open('players.json', 'r+', encoding="utf-8")
        json.load(players)
        players_list = players['players']
        if 429991199865307138 in players_list:
            print("True")
        else:
            print("False")


@client.event
async def on_member_update(before, after):
    return


client.run(TOKEN)