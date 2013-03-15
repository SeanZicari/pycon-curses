from urllib2 import urlopen
from xml.sax.saxutils import unescape
from simplejson import loads


def get_joke():
    return loads(urlopen('http://api.icndb.com/jokes/random').read())

for i in xrange(1, 5):
    print "Quote %d" % i
    print get_joke()['value']['joke']