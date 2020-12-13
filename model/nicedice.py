# nicedice.py
# This file is the main collection of modules used to roll dice for the discord bot
# You can test the below code using the following command
# python3 -m pytest model/nicedice.py
import os
import re
import json
import dice
import discord
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def dice_roll(self, message):
    messageoper = None
    messagesplit = None

    if "+" in message.content or "-" in message.content:
        dice_roll_multi()
    elif "DL" in message.content:
        with open('model/dicerolltypes.json') as rolltypes:
            rolltypedata = json.load(rolltypes)
        drollboyddice = dice_roll_body(message,rolltypedata["DL"])
        return drollboyddice
    elif "body" in message.content:
        with open('model/dicerolltypes.json') as rolltypes:
            rolltypedata = json.load(rolltypes)
        drollboyddice = dice_roll_body(message, rolltypedata["body"])
        return drollboyddice
    else:
        droll = dice_roll_basic()

    messagesplit, messageoper = get_roll_type(message)

    # Roll using the dice module    
    droll = dice.roll(messagesplit)

    # Handle the output
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

    return drollresult

def dice_roll_multi(self, arr_dicerolls):
    pass

def dice_roll_basic(self, diceroll):
    pass

def dice_roll_body(self, bodydice):
    droll = dice.roll("1d" + str(len(bodydice)))[0]
    bodypart = bodydice[droll]
    return bodypart

def get_dice_result(self, droll, message):
    # Handle the output
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

    return drollresult

def get_roll_type(self, message):
    if "+" in message.content or "-" in message.content: 
        messageoper = re.search("[\-\+]", message.content.split("/roll")[1])
        messagesplit = (message.content.split("/roll")[1]).split("+")[1]
    else:
        messagesplit = (message.content.split("/roll")[1])
        messageoper = None

    return messagesplit, messageoper

def get_requested_dice(self, message):
    if "+" in message.content or "-" in message.content: 
        messageoper = re.search("[\-\+]", message.content.split("/roll")[1])
        messagesplit = (message.content.split("/roll")[1]).split("+")[1]
    else:
        messagesplit = (message.content.split("/roll")[1])
        messageoper = None

    return messagesplit, messageoper

def dice_roll_math(self):
    pass

def sanitize_input(self, inputs):
    # Return a message if the input is not valid
    pass

# Work on exception catching

#client.run(TOKEN)