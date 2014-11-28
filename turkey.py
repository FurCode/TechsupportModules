# RoboCop 2's turkey.py, written during Thanksgiving 2014. Serves some delicious stuff!
# Adapted from Original Robocop's turkey.py
# coding=utf-8
import re
import random

from cloudbot import hook

cakes = ['oven-roasted turkey', 'honey-glazed ham', 'orange turkey', 'roast turkey', 'fried turkey', 'citrus-marinated turkey', 'honey-mustard glazed ham', 'baked ham', 'pork ham', 'honey glazed turkey']


@hook.command
def turkey(text, action=None):
    """turkey <user> - [Thanksgiving 2014] Serves <user> some thanksgiving turkey (or ham)."""
    text = text.strip()

    if not re.match("^[A-Za-z0-9_|.-\]\[]*$", text.lower()):
        return "Nope, no turkey for that user!"

    turkey_type = random.choice(cakes)
    size = random.choice(['small', 'little', 'mid-sized', 'stuffed', 'large', '10lb'])
    flavor = random.choice(['tasty', 'delectable', 'delicious', 'yummy', 'filling', 'scrumptious', 'mouthwatering'])
    method = random.choice(['makes', 'gives', 'gets', 'buys'])
    side_dish = random.choice(['mashed potatoes', 'pumpkin pie', 'squash soup', 'cranberry sauce'])

    action("{} {} a {} {} {} and serves it with a side of {}!".format(method, text, flavor, size, turkey_type, side_dish))
