# bot.py
# region Library
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
        await message.channel.send('{}'.format(message.author.mention) + ", starting download, might take a minute or two.")
        all_args = message.content.split()
        url = all_args[2]
        if len(all_args) < 3:
            await message.channel.send('{}'.format(message.author.mention) + ", you did not provide URL !")
            return
        dl_file = downloader.download_as_mp3(url)
        await message.channel.send('{}'.format(message.author.mention) + ", you download is ready !", file = discord.File(dl_file))
        os.remove(dl_file)

if __name__ == "__main__":
    client.run(TOKEN)