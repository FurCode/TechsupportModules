from util import hook
import random

@hook.command
def gduran144(inp, conn=None ):
        value = random.randint(0, 6)
        if value == 2:
                conn.cmd("KICK #eisenstein GDuran144 Someone got you kicked!")
                return "*BANG*";
        else:
                return "He got lucky this time...";
