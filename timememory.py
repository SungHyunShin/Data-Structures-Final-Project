#!/usr/bin/env python3
import os
import sys
import random

nlas = [1,2,3,4];
nlls = [1,2,3,4,5];


URL = "https://en.wikipedia.org/wiki/Fortnite";

# Heading
print("Wikipedia Article URL: " + URL)
print(" ")
print("| {:^12}| {:^12}| {:^13}| {:^13}|".format("#LINKS", "#LAYERS", "Time Usage", "Memory Usage"))
print("|{:-<13}|{:-<13}|{:-<13} |{:-<13} |".format("-", "-", "-","-", "-"))

# Content
for nla in nlas:
	for nll in nlls:
		command = "./measure ./wikiCrawler.py -l " + URL + " -nla " + str(nla) + " -nll " + str(nll) + " | tail -1"
		output = os.popen(command).read().split()
		time = output[0]
		memory = output[2]
		print("| {:<12}| {:<12}| {:<13}| {:<13}|".format(str(nll), str(nla), time, memory))



# End
print("|{:-<13}|{:-<13}|{:-<14}|{:-<14}|".format("-", "-", "-", "-", "-"))
