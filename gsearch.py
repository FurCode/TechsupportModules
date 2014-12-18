# RoboCop Classic's gsearch.py - A backport of gsearch.py from RoboCop 2 for the older CloudBot engine.
# This Module requires a Google Custom Search API key and a Custom Search Engine ID in order to function.
# Contact foxlet at inquries@comprepair.tk for support with this module.

import random

from pprint import pprint
import urllib, urllib2

from util import hook, http, text


def api_get(query):
    """Use the RESTful Google Search API"""
    # YOU NEED A KEY TO USE THIS MODULE!!!
    # [key] is your Google Developers Project API Key, and [cx] is the custom search engine ID to use for requests.
    key = urllib.quote('KEY_HERE')
    cx = urllib.quote('CSE_ID_HERE')

    url = 'https://www.googleapis.com/customsearch/v1?cx=' + cx + '&q='+ query + '&key=' + key
    return http.get_json(url)

@hook.command('gsearch')
@hook.command('gse')
@hook.command
def gse(inp):
    """gsearch <query> -- Returns first google search result for <query>."""

    eval = urllib.quote(inp)
    parsed = api_get(eval)

    result = parsed['items'][0]

    title = http.unescape(result['title'])
    title = text.truncate_str(title, 60)
    content = http.unescape(result['snippet'])

    if not content:
        content = "No description available."
    else:
        content = http.html.fromstring(content).text_content()
        content = text.truncate_str(content, 150)

    return u'{} -- \x02{}\x02: "{}"'.format(result['link'], title, content)
