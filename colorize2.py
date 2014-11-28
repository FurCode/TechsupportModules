# RoboCop 2's Colorize2.py - The text colorization module allows the coloring of any text, even on clients without support for it.

from cloudbot import hook
import random

@hook.command
def colorize(text):
	"""[color|random];[text] - colorizes the text input to the color provided."""
	arguments = text.split(";")
	color = arguments[0].lower()
	text = arguments[1]
	if color == "white":
		return "0" + text;
	elif color == "black":
		return "1" + text;
	elif color == "navyblue":
		return "2" + text;
	elif color == "green":
		return "3" + text;
	elif color == "red":
		return "4" + text;
	elif color == "brown":
		return "5" + text;
	elif color == "purple":
		return "6" + text;
	elif color == "orange":
		return "7" + text;
	elif color == "yellow":
		return "8" + text;
	elif color == "lightgreen":
		return "9" + text;
	elif color == "teal":
		return "10" + text;
	elif color == "cyan":
		return "11" + text;
	elif color == "blue":
		return "12" + text;
	elif color == "pink":
		return "13" + text;
	elif color == "grey":
		return "14" + text;
	elif color == "lightgrey":
		return "15" + text;
	elif color == "random":
		letters = list(text)
		string = "";
		for x in letters:
			value = "%02d" % random.randint(0, 15)			
			string += "" + str(value) + x + ""
		return string
	else:
		return "\'"+ color + "\' is not a valid color.";

