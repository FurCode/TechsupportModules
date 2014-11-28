# RoboCop 2's rules.py - A rules command designed specifically for #techsupport on Snoonet (IRC)

from cloudbot import hook

@hook.command
def rules(text, conn=None, chan=None):
	"""[spam|nick|nocoop|abuse|none] <user> - rules command for #techsupport."""
	if " " in text:
		command,user = text.split(" ")
		if command == "spam":
			return user + ": Your issue was too long. Go to http://pastebin.com and link your issue from there.";
		if command == "nick":
			return user + ": Please change your nick by typing /nick my_nickname";
		if command == "nocoop":
			return user + ": You've been helped on the matter and will receive no further help or advice. Thank you for your (non-existent) cooperation.";
		if command == "abuse":
			return user + ": Abusing the bot might cause you to be kicked from the channel, please refrain from it.";
	else:
		if text == "debug":
			conn.cmd("PRIVMSG " + chan + " This is a debug message. Thank you for listening.");
		else:
			bienvenue = "Welcome to #techsupport! | Do not ask for help or specific skills, just state your issue. | For verbose descriptions, use a pastebin or a link to your /r/techsupport thread. | Generic nicks must be changed by typing /nick <nickname>. | Please be patient and don't spam.";
			if text == "":
				return bienvenue;
			else:
				return text + ": " + bienvenue;
