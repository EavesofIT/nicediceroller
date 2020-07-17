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


        if "+" in message.content or "-" in message.content:
            messageoper = re.search("[\-\+]", message.content.split("/roll")[1])
            messagesplit = (message.content.split("/roll")[1]).split("+")
            print("messagesplit")
            print(messagesplit)
            droll = dice.roll(messagesplit[0])
            if isinstance(droll, list):
                drollsum = sum(droll)
                drollresult = drollsum
            else:
                drollresult = droll
            if messageoper.group() == "-":
                drollsum = drollresult - int(messagesplit[1])
            else:
                drollsum = drollresult + int(messagesplit[1])

            drollresult = "You rolled " + str(droll) + " " + str(messageoper.group()) + " " + messagesplit[1] + " = " + str(drollsum)

        print(drollresult)

        await channel.send(drollresult)
        
client.run(TOKEN)