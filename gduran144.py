from util import hook
import random

@hook.command
def gduran144(inp, conn=None, chan=None, action=None):
        value = random.randint(0, 6)
        if value == 2:
                action("*BANG*")
                conn.cmd("KICK " + chan + " GDuran144 Do the Truffle Shuffle!");
        else:
                return "He got lucky this time...";
