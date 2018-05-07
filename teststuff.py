#!/usr/bin/env python3 
import os


f= open("test.file.txt","w+")
os.popen("valgrind ./wikiCrawler.py -l https://en.wikipedia.org/wiki/Fortnite -nla 3 -nll 3 | grep suppressed > test.file.txt")


statinfo = os.stat("test.file.txt")

if(statinfo.st_size == 0):
    print('No memory errors')
else:
    print('There are leaks')


