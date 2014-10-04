from util import hook
import os

def announce(text, conn, chan, action=None, nick=None):
	conn.cmd("PRIVMSG " + chan + " " + str(text));

@hook.command('summon', permissions=["botcontrol"], autohelp=False)
def summon(inp, chan=None, conn=None):
	if chan == "#eisenstein":
		if inp == "!all":
			open("summonlist.txt", 'a').close()
			conn.cmd("WHO", [chan])
		else:
			return "Calling " + inp + "."
			
@hook.event('352')
def who_summon(inp, conn=None, chan="#eisenstein"):
	user = str(inp[5]);
	store(user + ";")
	
@hook.event('315')
def end_summon(inp, conn=None, chan="#eisenstein"):
	usrlist = retreive()
	del usrlist[-1]
	prettylist = ', '.join(usrlist)
	announce(prettylist, conn, "#eisenstein");
	os.remove("summonlist.txt")

def store(data):
	try:
		# MORE FUNCTIONS!!!
		logfile = open("summonlist.txt", "a")
		try:
			logfile.write(data)
		finally:
			logfile.close()
	except IOError:
		pass
        
def retreive():
	try:
		f = open("summonlist.txt", "r")
		try:
			# Read the entire contents of a file at once.
			args = f.read()
		finally:
			f.close()
	except IOError:
		string = "Could not read file."
	arguments = args.split(";")
	return arguments;