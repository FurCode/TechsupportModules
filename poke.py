from util import hook

@hook.command
def poke(inp, chan=None, conn=None, action=None):
	action("pokes " + inp);