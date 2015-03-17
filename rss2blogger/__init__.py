import sys
import urllib2
import feedparser

class RSS2Blogger():
	def __init__(self, url=None):
		self.url=url

	def display(self):
		f=feedparser.parse(self.url)
	
		for entry in f.entries:
			print entry.title+' - '+entry.link+' - '+entry.published+"\n"


