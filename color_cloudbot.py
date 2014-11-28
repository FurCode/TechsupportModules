# RoboCop 2's color_cloudbot.py - Color and Rainbow mods for text.

from cloudbot import hook

@hook.command
def rainbow(text):
	palette = {1: '04', 2: '07', 3: '08', 4: '09', 5: '11', 6: '12', 7: '06'};
	string = text;
	sloop = len(string);
	stack = 0
	letters = list(string);	
	mod = "";

	for x in range(0, sloop):
		if stack == 7:
			stack = 0;
		stack += 1;
		mod += palette.get(stack) + letters[x];
	return mod;
