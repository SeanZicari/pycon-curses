from urllib2 import urlopen
from HTMLParser import HTMLParser
from simplejson import loads


def get_new_quote():
    new_quote = urlopen('http://www.iheartquotes.com/api/v1/random?format=json').read()
    return HTMLParser().unescape(loads(new_quote)['quote']).encode('utf-8')


def get_new_joke():
    joke_json = loads(urlopen('http://api.icndb.com/jokes/random').read())
    return HTMLParser().unescape(joke_json['value']['joke']).encode('utf-8')
