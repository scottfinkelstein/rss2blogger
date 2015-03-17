from setuptools import setup

setup(
	name='rss2blogger',
	version='0.1',
	description='Simple script for porting RSS posts to a Blogger blog.',
	url='http://scottfinkelstein.com',
	author='Scott Finkelstein',
	author_email='sbf0202@gmail.com',
	license='MIT',
	packages=['rss2blogger'],
	install_requires=[
		'feedparser'
	],
	zip_safe=False
)
