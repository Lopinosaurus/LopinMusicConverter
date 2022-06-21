# bot.py
# region Library
import os
import system_functions
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
    await client.change_presence(activity = discord.Game(name="$start | You are a fucking nerd"))

@client.event
async def on_message(message):
    # Ignore self messages
    if message.author == client.user:
        return

    if message.content.lower().startswith('$start'):
        if system_functions.is_registered(message.author):
            await message.channel.send('{}'.format(message.author.mention) + ", your League of Legends games are already looked up !")
        else:
            system_functions.watch_games(message.author)
            await message.channel.send('{}'.format(message.author.mention) + ", your games are now registered !")


@client.event
async def on_member_update(before, after):
    if before.activity == after.activity:
        return

    if not system_functions.is_registered(before):
        return

    if (not system_functions.is_playing_lol(before)) and system_functions.is_playing_lol(after):
        system_functions.start_time(after)
        return

    if system_functions.is_playing_lol(before) and not system_functions.is_playing_lol(after):
        system_functions.add_global_time(after)
        return

client.run(TOKEN)