from util import hook
import feedparser
import random

@hook.command
def furry(inp):
	d = feedparser.parse('http://backend.deviantart.com/rss.xml?type=deviation&q=furry')
	counter = len(d['entries'])
	value = random.randint(0, counter)
	returnitem = d.entries[value]['link'] 
	return str(returnitem)

#Single Liner Code	
#import feedparser; import random; d = feedparser.parse('http://backend.deviantart.com/rss.xml?type=deviation&q=furry'); counter = len(d['entries']); value = random.randint(0, counter); returnitem = d.entries[value]['link']; print str(returnitem);

p/tF CClU S/nb 3c9g yuzQ jCFH UqZ7 9+c9 WNyi ZamZ vis=
1045-0718-9240-3524-3964-7785
9119-9827-1529-4594-2858
p/tF CClU S/nb 3c9g yuzQ jL9R Aalc lTCI pyqg 7FLo hEY=

°F