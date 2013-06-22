#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import sqlite3


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
	
	#디비 연결
	db = sqlite3.connect("../what_to_eat")
	cursor = db.cursor()
	cursor.execute("select * from recommend_food_categories where Name='한식'")

	category_pk = 0
	for row in cursor:
		category_pk = row[0]
		
	cursor.execute("select * from recommend_food_regions where Name='학교'")

	region_pk = 0
	for row in cursor:
		region_pk = row[0]

	cursor.execute("delete from recommend_food_restaurants where Name='302동'")

#고쳐야함 ㅡㅡ
	data = [(1, None), (2, u'302동'), (3, category_pk), (4, u'몰라'), (5, region_pk), (6, None)]
	query = "insert into recommend_food_restaurants('302동', '"
	query += str(category_pk)
	query += "', '몰라', '"
	query += str(region_pk)
	query += "')"
	print(query)
#cursor.execute(query)
	cursor.executemany("insert into recommend_food_restaurants values (?, ?, ?, ?, ?, ?)", data)


	cursor.close()



	fh.close()



main()













