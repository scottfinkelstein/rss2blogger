import sys
import urllib2
import feedparser

def main():
	f=feedparser.parse('http://adelphi-tech.blogspot.com/feeds/posts/default')
	
	for entry in f.entries:
		print entry.title+' - '+entry.link+' - '+entry.published+"\n"

if __name__ == '__main__':
	main()

