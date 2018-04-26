#!/usr/bin/env python3

import sys 
import os
from bs4 import BeautifulSoup
import requests
import random
import string

def random_string(length):
	return ''.join(random.choice(string.ascii_letters) for m in range(length))

URL = "https://en.wikipedia.org/wiki/Main_Page"
LAYERS = 1
NUM_LINKS = 6

def usage(status = 0):
	print(''' Usage:
		-h 	HELP 		Display usage message 
		-l	LINK		Provide a wikipedia link
		-nla	NUM_LAYERS	Provide the number of layers  
		-nll	NUM_LINKS	Provide number of links to expand)
	''')
	sys.exit(status)

def getlinks(url, filenum, linknum, layers):
	if layers > LAYERS:
		return

	source = requests.get(url)
	data = source.text
	soup = BeautifulSoup(data,"html.parser")
	
	f = open("links.txt","w+")
	
	for link in soup.find_all('a'):
		if (link.get('href','').startswith('/wiki/') and not link.get('href','').startswith('/wiki/Special:') and not link.get('href','').startswith('/wiki/Help:') and not link.get('href','').startswith('/wiki/Category:') and not 
link.get('href','').startswith('/wiki/Wikipedia:About')):
			f.write(link.get('href'))
			f.write('\n')
	f.close()

	randstr = random_string(5)

#	putURLcommand = "echo \"" + url + "\" > toplinks" + str(layers) + str(filenum) + ".txt"
	putURLcommand = "echo \"" + url + "\" > " + randstr + ".txt"
	os.system(putURLcommand)
#	commandsort = "cat links.txt | sort | uniq -c | sort -n | tail -" + str(linknum) + " | sort -nr >> toplinks" + str(layers) + str(filenum) + ".txt"
	commandsort = "cat links.txt | sort | uniq -c | sort -n | tail -" + str(linknum) + " | sort -nr >> " + randstr + ".txt"

	os.system(commandsort)
	os.system("rm links.txt")

#	linkstr="toplinks"+str(layers)+str(filenum)+".txt"
	linkstr = randstr + ".txt"

	count = 0
	for lines in open(linkstr,"r").read().splitlines()[1:]:
		print(lines)
		lines = lines.split()
		count += 1
		newurl = "https://en.wikipedia.org" + lines[1]
		getlinks(newurl, filenum+count, linknum, layers+1)


# main
if len(sys.argv)==1:
	usage(0)

args = sys.argv[1:]
while (len(args) and args[0].startswith('-') and len(args[0])>1):
	arg = args.pop(0);
	if arg == '-h':
		usage(0)
	elif arg == '-l':
		URL = args.pop(0)
	elif arg == '-nla':
		LAYERS = int(args.pop(0))
	elif arg == '-nll':
		NUM_LINKS = int(args.pop(0))
	else:
		usage(1)

		
if not URL.startswith("https://en.wikipedia.org"):
	print("Invalid URL")
	usage(1)

getlinks(url=URL, filenum=0, linknum=NUM_LINKS, layers=0)
