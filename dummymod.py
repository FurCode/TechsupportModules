from util import hook

@hook.command
def dummymodule(inp):
	return "This is a dummy module. " + inp;