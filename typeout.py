from util import hook

@hook.command
def typeout(inp):
	cont = list(inp)
	prettyform = '.'.join(cont)
	caps = prettyform.upper()
	return str(caps)
