import urllib, urllib2
import lxml.html
from util import hook
import string
import random

def gname(size=8, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def store(moduledata):
	try:
		#This is the base directory of the modules folder
		basedir = "plugins/"
		filename = basedir + gname() + ".py"
		# This tries to open an existing file but creates a new file if necessary.
		plugins = open(filename, "w")
		try:
			plugins.write(moduledata)
		finally:
			plugins.close()
	except IOError:
		pass
		
@hook.command('rmodule', permissions=["botcontrol"])
def rmodule(inp):
	if inp == "help":
		return "The Remote Module-module allows RoboCop to load Python modules from the internet. Usage: @rmodule <http://example.com/linktomodule.py>";
	else:
		url = str(inp);
		data = urllib2.Request(url, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
		try:
			urlfile = urllib2.urlopen(data)
		except urllib2.HTTPError:
			return "That module could not be loaded, the server is not responding."
		module = urlfile.read()
		store(module)
		return "Module has been loaded. You may need to restart RoboCop to take effect."