import urllib2

reg = urllib2.Request('http://my.pretend.server')
response = urllib2.urlopen(reg)
the_page = response.read()
