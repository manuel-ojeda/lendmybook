"""
Here we manage the google books api for getting
book's name, authors, description, isbn code,
cover image, and possibly categories
"""

import requests

def getBookData(title,author):
	titlevar = title
	authorvar = author
	
	industryIdentifiers= "industryIdentifiers(identifier),"
	imageLinks = "imageLinks(thumbnail),"
	volumeInfo = "volumeInfo(title,authors,description,"+ imageLinks + industryIdentifiers + "categories)"
	items = "items(" + volumeInfo + ")"
	requieredFields = "&fields=" + items
	apiKey = "AIzaSyAKi3MX1SA_B6mw4iPGv0jN58Wn-xakQk4"
	
	if authorvar == "no conozco el autor":
		queryFields = "&q=intitle:" + titlevar +"&"
	else:
		queryFields = "&q=intitle:" + titlevar + ",inauthor:" + authorvar +"&"
	
	requesturl = "https://www.googleapis.com/books/v1/volumes?" + queryFields + apiKey + requieredFields
	
	response = requests.get(requesturl)

	r = response.json()
	
	allOptions = []

	for i in range (0,len(r["items"])):

		try:
			bookTitle = r["items"][i]["volumeInfo"]["title"]
		except:
			bookTitle = None

		try:
			bookAuthor = r["items"][i]["volumeInfo"]["authors"]
		except:
			bookAuthor = None

		try:
			bookDescription = r["items"][i]["volumeInfo"]["description"]
		except:
			bookDescription = None

		try:
			bookCover = r["items"][i]["volumeInfo"]["imageLinks"]["thumbnail"]
		except:
			bookCover = None

		try:
			bookCover2 = r["items"][i]["volumeInfo"]["industryIdentifiers"][0]["identifier"]
		except:
			bookCover2 = None

		try:
			bookCategories = r["items"][i]["volumeInfo"]["categories"]
		except:
			bookCategories = None

		option = [bookTitle,bookAuthor, bookDescription, bookCover,bookCover2,bookCategories]
		allOptions.append(option)

	return allOptions
