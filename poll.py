from util import hook
import os
import pickle

@hook.command
def poll(inp, conn=None, chan=None, action=None, nick=None):
	args = inp;
	if inp == "help":
		return "This does nothing.";
	if inp == "close":
		os.remove("plock.txt")
		tally = readtally();
		results = retreive();
		num = 0;
		printer = ""
		for x in results:
                        num = num + 1
                        item = x + " - " + str(tally.get(num)) + " |"
                        printer = printer + " " + item;
		os.remove("tally.pkl")
		os.remove("poll.txt")
		return "Results from poll: " + printer;
	if inp.isdigit():
		numtovote = int(inp)
		tally = readtally();
		print tally;
		try:
			count = tally.get(int(inp));
			tally[int(inp)] = count + 1
			storetally(tally);
			notice("Voted for: " + inp, conn, chan, nick);
		except TypeError:
			notice("That is not valid.", conn, chan, nick);
	if inp == "list":
		results = retreive();
		prettylist = ', '.join(results)
		print list();
		message = "Currently up for votes:";
		count = len(results)
		announce(message, conn, chan);
		num = 0
		printer = "";
		for x in results:
			num = num + 1
			item = str(num) + "- " + x + " | "
			printer = printer + " " + item;
			#announce(item, conn, chan);	
		announce(printer, conn,chan);
		announce(str(count) + " in total.", conn, chan);
	if ";" in args:
		if not os.path.exists("plock.txt"):
    			file("plock.txt", 'w').close()
		else:
			return "There is a poll currently running, close it with @poll close first."
                arguments = args.split(";")
		store(inp);
		num = 0
		tally = {};
		for x in arguments:
			num = num + 1
			tally[num] = 0;
		print tally
		storetally(tally);
		return arguments;
def store(data):
	try:
		# This tries to open an existing file but creates a new file if necessary.
		logfile = open("poll.txt", "w")
		try:
			logfile.write(data)
		finally:
			logfile.close()
	except IOError:
		pass

def retreive():
	try:
		f = open("poll.txt", "r")
                try:
                        # Read the entire contents of a file at once.
                        args = f.read()
                finally:
                        f.close()
        except IOError:
                string = "Could not read file."
        arguments = args.split(";")
	return arguments;

def list():
	data = retreive();

def announce(text, conn, chan, action=None, nick=None):
	conn.cmd("PRIVMSG " + chan + " " + str(text));

def notice(text, conn, chan, nick, action=None):
	conn.cmd("NOTICE " + nick + " " + str(text));

def storetally(tallydata):
	try:
                # This tries to open an existing file but creates a new file if necessary.
                with open('tally.pkl', 'wb') as output:
			pickle.dump(tallydata, output, pickle.HIGHEST_PROTOCOL)
        except IOError:
                pass

def readtally():
        # This tries to open an existing file but creates a new file if necessary.
        with open('tally.pkl', 'rb') as input:
                tallydata = pickle.load(input)
		return tallydata;
