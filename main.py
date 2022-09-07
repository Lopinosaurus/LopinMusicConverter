# bot.py
# region Library
from turtle import down
import discord
from dotenv import load_dotenv
import os
import downloader
#endregion

#region Pre-config
load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents().all()
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    await client.change_presence(activity= discord.Game(name="Open-Source Youtube mp3 converter"))
    print ("Downloader connected to Discord !")

@client.event
async def on_message(message):
    # Ignore self messages
    if message.author == client.user:
        return

    if message.content.startswith("dl mp3"):
        message.channel.send('{}'.format(message.author.mention) + ", starting download...")
        all_args = message.split()
        url = all_args[2]
        filetype = all_args[3]
        if len(all_args) < 3:
            await message.channel.send('{}'.format(message.author.mention) + ", you did not provide URL !")
            return
        dl_file = downloader.download_as_mp3(url)
        message.channel.send('{}'.format(message.author.mention) + ", you download is ready !", file = discord.File(dl_file))
        os.remove(dl_file)
