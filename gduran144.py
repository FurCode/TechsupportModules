from util import hook
import random

@hook.command
def gduran144(inp, conn=None, chan=None, action=None, nick=None):
        value = random.randint(0, 6)
        valuebackfire =  random.randint(0,60)
        if inp == "gerald-catz":
                return "Reel: http://vimeo.com/24735385";
        else:
                if value == 2:
                        action("*BANG*")
                        conn.cmd("KICK " + chan + " GDuran144 Do the Truffle Shuffle!");
                else:
                        if valuebackfire == 7:
                                action("\'s bullet ricochets.")
                                conn.cmd("KICK " + chan + " " + nick + " Sorry!");
                        else:
                                return "He got lucky this time...";
