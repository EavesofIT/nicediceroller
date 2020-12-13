# test_with_pytest.py
from model import nicedice
import os
import re
import dice
import discord
from os.path import join, dirname
from dotenv import load_dotenv

""" 
def test_always_passes():
    assert True

def test_always_fails():
    assert False
 """

#def test_basic_diceroll():
#    assert nicedice.dice_roll("/roll 1d4")

def test_body_diceroll():
    assert nicedice.dice_roll_body("/roll body")

def test_DL_diceroll():
    with open('model/dicerolltypes.json') as rolltypes:
        rolltypedata = json.load(rolltypes)
    drollboyddice = nicedice.dice_roll_body(rolltypedata["DL"])
    return drollboyddice

def test_body_diceroll():
    with open('model/dicerolltypes.json') as rolltypes:
        rolltypedata = json.load(rolltypes)
    assert nicedice.dice_roll_body("/roll body")