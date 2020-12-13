# bot.py
import os
import re
import dice
import discord
from os.path import join, dirname
from dotenv import load_dotenv
import nicedice

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('/roll'):
        channel = message.channel
        await channel.send('Rolling dem dice!')

        #drollresult = nicedice.dice_roll(message)

        await channel.send(drollresult)

client.run(TOKEN)