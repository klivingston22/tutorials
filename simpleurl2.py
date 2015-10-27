import urllib2

reg=urllib2.Request('http://www.voidspace.org.uk')
response=urllib2.urlopen(reg)
the_page=response.read()
