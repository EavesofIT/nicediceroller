# bot.py
import os
import re
import dice
import discord
from os.path import join, dirname
from dotenv import load_dotenv

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

        messageoper = None

        if "+" in message.content or "-" in message.content:
            messageoper = re.search("[\-\+]", message.content.split("/roll")[1])
            messagesplit = (message.content.split("/roll")[1]).split("+")[0]
        else:
            messagesplit = (message.content.split("/roll")[1])
        droll = dice.roll(messagesplit)
        if isinstance(droll, list):
            drollsum = sum(droll)
            drollresult = drollsum
        else:
            drollresult = droll
        if "-" in message.content:
            drollsum = drollresult - int(messagesplit[1])
        elif "+" in message.content:
            drollsum = drollresult + int(messagesplit[1])
        if "+" in message.content or "-" in message.content:
            drollresult = "You rolled " + str(droll) + " " + str(messageoper.group()) + " " + messagesplit[1] + " = " + str(drollsum)
        else:
            drollresult = "You rolled " + str(droll) + " = " + str(drollsum)

        await channel.send(drollresult)
        
client.run(TOKEN)