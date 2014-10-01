from util import hook

@hook.command
def spellout(inp):
	cont = list(inp)
	prettyform = ' '.join(cont)
	caps = prettyform.upper()
	return str(caps)
