"""Searches the Techsupport Knowledgebase for available articles
by rod156 based on module by Scaevolus 2009"""

import re

from util import hook, http, text


api_prefix = "http://kb.comprepair.tk/kb/api.php"
search_url = api_prefix + "?action=opensearch&format=xml"

paren_re = re.compile('\s*\(.*\)$')


@hook.command('kb')
@hook.command
def kb(inp):
    """kb <topic> -- Gets the first article available on <topic>."""

    x = http.get_xml(search_url, search=inp)

    ns = '{http://opensearch.org/searchsuggest2}'
    items = x.findall(ns + 'Section/' + ns + 'Item')

    if not items:
        if x.find('error') is not None:
            return 'error: %(code)s: %(info)s' % x.find('error').attrib
        else:
            return 'No results found.'

    def extract(item):
        return [item.find(ns + x).text for x in
                ('Text', 'Description', 'Url')]

    title, desc, url = extract(items[0])

    if 'may refer to' in desc:
        title, desc, url = extract(items[1])

    title = paren_re.sub('', title)

    if title.lower() not in desc.lower():
        desc = title + desc

    desc = u' '.join(desc.split())  # remove excess spaces

    desc = text.truncate_str(desc, 200)

    return u'{} :: {}'.format(desc, http.quote(url, ':/'))