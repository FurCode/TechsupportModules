from util import hook
import feedparser

@hook.command
def furry(inp):
	d = feedparser.parse('http://backend.deviantart.com/rss.xml?type=deviation&q=furry')
	counter = len(d['entries'])
	value = random.randint(0, counter)
	returnitem = d.entries[value]['link'] 
	return str(returnitem)