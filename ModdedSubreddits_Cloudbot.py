from bs4 import BeautifulSoup
import urllib, urllib2
import lxml.html
from util import hook

@hook.command
def mods(inp):
	"""Usage: @mods [user]"""
	address = "http://www.reddit.com/user/" + inp
	data = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
	try:
		urlfile = urllib2.urlopen(data)
	except urllib2.HTTPError:
		return "Huh, that user seems to not exist."
	page = urlfile.read()
	soup = BeautifulSoup(page)
	
	#Title Message for the console
	print soup.title.string

	subreddits = soup.findAll("ul", { "id" : "side-mod-list" })
	user = inp
	
	#Return the list of subreddits
	try:
		list = str(subreddits[0])
	except IndexError:
		return "That user does not moderate anything."
	clean_list = lxml.html.fromstring(list).text_content() 
	table = clean_list.split("/r/")
	del table[0]
	prettylist = ', '.join(table)
	return "\x02" + user + "\x02" + " moderates: " + str(prettylist)