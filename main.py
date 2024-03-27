import discord
import os
from url_shortener import *
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Hello World')

@client.event 
async def on_message(message):
    key_word = '^shorten'

    if (key_word in message.content):
        link = message.content.replace(key_word, '')

        short_link = get_url(link)

        if short_link:
            await message.channel.send(short_link)



client.run(TOKEN)