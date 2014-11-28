# RoboCop 2's fox.py - Brings a cute fox submission from the /r/foxes subreddit

from cloudbot import hook
import feedparser
import random

@hook.command
def foxes(text):
	d = feedparser.parse('https://www.reddit.com/r/foxes/.rss')
	counter = len(d['entries'])
	print(counter);
	value = random.randint(0, counter)
	url = d.entries[value]['link']
	print(url);
	link = reddit_small(url)
	returnitem = d.entries[value]['title'] + " - " + link 
	return str(returnitem)

def reddit_small(url):
	baseurl = "http://redd.it/"
	urlid = url[40:]
	shortid = urlid[:6]
	return baseurl + shortid
