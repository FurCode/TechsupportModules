from cloudbot import hook
import random
import time
import json
import urllib.parse
import urllib.request

@hook.command
def octosearch(text, conn=None, chan=None, action=None, nick=None):
	"""octosearch <keyword> -- Search for any part on Octopart."""
	url = "http://octopart.com/api/v3/parts/search"

	# NOTE: Use your API key here (https://octopart.com/api/register)
	url += "?apikey=aefcd00e" 

	args = [
	   ('q', text),
	   ('start', 0),
	   ('limit', 2)
	   ]

	url += '&' + urllib.parse.urlencode(args)

	data = urllib.request.urlopen(url).read()
	search_response = json.loads(data.decode("utf-8"))

	# print number of hits
	numhits = search_response['hits']
	conn.cmd("PRIVMSG " + chan + " Number of Hits: " + str(numhits));

	# print results
	for result in search_response['results']:
	   part = result['item']

	   # print matched part
	   numresult = "%s - %s - %s" % (part['brand']['name'], part['mpn'], part['octopart_url'])
	   conn.cmd("PRIVMSG " + chan + " " + numresult);
