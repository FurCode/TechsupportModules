from util import hook
import re

pattern = re.compile('^Snoo\d+$')
pattern2 = re.compile('^Guest\d+$')

@hook.command('guests', permissions=["botcontrol"], autohelp=False)  # you can replace "botcontrol" with your desired permission, or 'guestout' with a better command name
def rampage(inp, chan=None, conn=None):
    conn.cmd("WHO", [chan])


@hook.event('352')
def who_rampage(inp, conn=None):
	if pattern.match(inp[5]):
		conn.cmd("KICK", [inp[1], inp[5], "Please change your nick from the default and come back!"])
	if pattern2.match(inp[5]):
		conn.cmd("KICK", [inp[1], inp[5], "Please change your nick from the default and come back!"])
