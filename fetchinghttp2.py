import urllib2

reg = urllib2.Request('http://www.pretend_server.org')

try: urllib2.urlopen(reg)
except urllib2.HTTPError as e:
	print e.code
	if e.code == 404
		print "file not found"
else:
	print 'site is up'
	code = urllib2.urlopen(reg).getcode()

if code == 200:
	print '200 - OK'
elif code == 404:
	print '404 - Not Found'
elif code == 500:
	print '500 - Internal Server Error'
else:
	print 'NO CODE'