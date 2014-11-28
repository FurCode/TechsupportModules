# RoboCop 2's about.py - This module simply gives information about the bot, licenses, and authors.
# based upon gpl.py and maintainer.py, from the original RoboCop.

from cloudbot import hook

@hook.command
def gpl(text):
	"""[info|license] - gives information about getting source code, or finding the license for the bot"""
	if text == "license":
		return "RoboCop is licensed under the GPL v3 license. The terms are available at https://github.com/FurCode/TechsupportModules/blob/master/LICENSE"
	else:
		return "Please email RoboCop@comprepair.tk or go to https://github.com/FurCode/TechsupportModules"

@hook.command
def about():
	return "RoboCop 2 is a fork of CloudBot Refresh, designed to feel like classic RoboCop. Written by rodthefox, maintained by the #techsupport team. (c) FurCode 2014"
