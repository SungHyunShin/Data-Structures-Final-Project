#!/usr/bin/env python3
import sys 
import os
from bs4 import BeautifulSoup
import requests

def getlinks(url="https://en.wikipedia.org/wiki/Main_Page", filenum = 0):
	source = requests.get(url)
	data = source.text
	soup = BeautifulSoup(data,"html.parser")
	numnode = input("Enter the number of links to be shown: ")
	
	f = open("links.txt","w+")
	
	for link in soup.find_all('a'):
		if (link.get('href','').startswith('/wiki/') and not link.get('href','').startswith('/wiki/Special:')):
			f.write(link.get('href'))
			f.write('\n')
	f.close()
	commandsort = "cat links.txt | sort | uniq -c | sort -n | tail -" + str(numnode) + " | sort -nr > toplinks" + str(filenum) + ".txt"
	os.system(commandsort)
	os.system("rm links.txt")


# main
layers = int(input("Enter layers: "))
url = input("Please enter a wikipedia url: ")
while not url.startswith("https://en.wikipedia.org"):
	print("Invalid URL")
	url = input("Enter a new URL: ")

count = 0;
while layers>0:
	getlinks(url, count)
	linkstr="toplinks"+str(count)+".txt"
	for lines in open(linkstr,"r").read().splitlines():
		count += 1
		lines = lines.split()
		newurl = "https://en.wikipedia.org" + lines[1]
		getlinks(newurl, count)
	layers -= 1


