#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import subprocess
from ../recommend_food.models import Categories

def removeSpace(fh):
	document = ""

	for line in fh:
		line = line.strip()
		line = line.replace(" ", "")
		line = line.replace("	", "")
		line = line.replace("\n", "")
		document += line
	return document

def splitMenu(string):
	l = []
	if "<br>" in string:
		l = string.split("<br>")
	else:
		l = [string]

	result = []
	for elem in l:
		if elem[0] == "(":
			elem = elem[1:]
		g = elem.split(")")
		result.append(g)

	return result


def main():
	fh = open("menu.html")

	html = removeSpace(fh)
	tableStart = html.find("<table")
	tableEnd = html.find("</table>")
	tableString = html[tableStart:tableEnd]
	trString = ""
	start = 0

	menuStart = tableString.find("919동")
	menuEnd = tableString.find("</tr", menuStart)
	menuString = tableString[menuStart:menuEnd]

	start = menuString.find("(")
	end = menuString.find("&nbsp")
	breakfast = ""
	if start != -1:
		breakfast = menuString[(start + 1):end]
		breakfast = splitMenu(breakfast)
	menuString = menuString[(end + 6):]
	print(breakfast)
	
	start = menuString.find("(")
	end = menuString.find("&nbsp")
	lunch = ""
	if start != -1:
		lunch = menuString[(start + 1):end]
		lunch = splitMenu(lunch)
	menuString = menuString[(end + 6):]
	print(lunch)

	start = menuString.find("(")
	end = menuString.find("&nbsp")
	dinner = ""
	if start != -1:
		dinner = menuString[(start + 1):end]
		dinner = splitMenu(dinner)
	print(dinner)
	

	fh.close()



main()













