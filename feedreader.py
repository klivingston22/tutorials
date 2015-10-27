import feedparser

feeddata = feedparser.parse('http://www.reddit.com/r/python/.rss')

print feeddata['entries'][0]['title']

for post in feeddata.entries:

	print post.title + ":" + post.link + "\n"

limit = 5





