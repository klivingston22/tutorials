import urllib2

reg = urllib2.Request('http://www.rgu.ac.uk')

try: urllib2.urlopen(reg)
except urllib2.URLError as e:
	print e.reason
else:
	print 'site is up'
	code = urllib2.urlopen(reg).getcode()
	print code