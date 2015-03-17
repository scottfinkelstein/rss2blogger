import sys
import urllib2
import feedparser

class RSS2Blogger():
	def display(self):
		f=feedparser.parse('http://adelphi-tech.blogspot.com/feeds/posts/default')
	
		for entry in f.entries:
			print entry.title+' - '+entry.link+' - '+entry.published+"\n"


