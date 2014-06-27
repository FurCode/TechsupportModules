from util import hook

@hook.command('welcome')
def echo(inp):
        if inp == "debug":
                return "Welcome back /User/!"
#test
