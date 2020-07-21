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

        if "help" in message.content or "-h" in message.content:
            help = dice_help()
            await channel.send(help)
            return
        else:
            await channel.send('Rolling dem dice!')

            messageoper = None

            if "+" in message.content or "-" in message.content: 
                messageoper = re.search("[\-\+]", message.content.split("/roll")[1])
                messagesplit = (message.content.split("/roll")[1]).split("+")[1]
            else:
                messagesplit = (message.content.split("/roll")[1])

            try:
                droll = dice.roll(messagesplit)
            except dice.DiceBaseException as e:
                await channel.send()

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

def dice_help():
    help = "The roll command can be used to roll multiple styles of roll such as 1d6, 1d6+2, DL, body part, etc"
    return help

def dice_roll(self, arr_dicerolls):
    pass

def dice_roll_basic(self, diceroll):
    pass

def dice_roll_dl():
    pass

def sanitize_input(self, inputs):
    # Return a message if the input is not valid
    pass

# Work on exception catching

client.run(TOKEN)