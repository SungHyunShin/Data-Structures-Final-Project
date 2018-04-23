#!/usr/bin/env python3

import sys 
import os
from bs4 import BeautifulSoup
import requests

url = input("Enter a link: ")
source = requests.get(url)
data = source.text
soup = BeautifulSoup(data,"html.parser")
numnode = input("Enter the number of links to be shown: ")

f = open("links.txt","w+")
 
for link in soup.find_all('a'):
	if (link.get('href','').startswith('/wiki/') and not link.get('href','').startswith('/wiki/Special:')):
		f.write(link.get('href'))
		f.write('\n')

commandsort = "cat links.txt | sort | uniq -c | sort -n | tail -" + str(numnode) + " | sort -nr > toplinks.txt"
os.system(commandsort)
os.system("rm links.txt")

