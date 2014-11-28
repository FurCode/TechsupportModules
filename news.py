# RoboCop 2's news.py, picks a random article from Google News.

from cloudbot import hook
import feedparser
import random

@hook.command
def news(text):	
	d = feedparser.parse('https://news.google.com/news/feeds?pz=1&cf=all&ned=us&hl=en&output=rss')
	counter = len(d['entries'])
	value = random.randint(0, counter)
	returnitem = d.entries[value]['title'] 
	return str(returnitem)
