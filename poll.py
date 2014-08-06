from util import hook
import os

@hook.command
def poll(inp, conn=None, chan=None, action=None, nick=None):
	args = inp;
	if inp == "help":
		return "This does nothing.";
	if inp == "close":
		os.remove("plock.txt")
		return "Results from poll: ";
	if inp.isdigit():
		return "Voted for:" + inp;
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
