import requests
from bs4 import BeautifulSoup

# Importing materials for creating out GUI
# Creating a simple GUI: https://realpython.com/pysimplegui-python/
# Yt vid: https://www.youtube.com/watch?v=jE-SpRI3K5g
import tkinter as tk
from tkinter import filedialog, Text
import os

# https://realpython.com/beautiful-soup-web-scraper-python/#why-scrape-the-web
# This website is great for getting started!

# Using BeautifulSoup for Web Scraping news articles
# https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558 

# Setting up our URL
URL = 'https://www.nytimes.com/2021/09/18/world/covid-trash-recycling.html?searchResultPosition=1'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Global variable used for our author(s)
authorList = []

def printAuthors(authorlist):
    # TODO: Make sure you get rid of the random 'u' in front of each string element
    # print(authorList)
    for author in authorList:
        print("\t" + "* "  + author)


def articleInfo(url):
    # Printing the source name (works abstractly)
    arrayWeb = URL.split('/')
    siteName = arrayWeb[2]

    # Saving the title
    title = soup.title.string

    # Saving the author(s)
    authors = soup.find_all(class_='css-ozn3l9 e1jsehar0')
    
    # Checking for the number of authors
    if len(authors) == 1:
        author1 = str(authors[0])
        newSoup = BeautifulSoup(author1, 'html.parser')
        authorName = newSoup.a.string
        authorList.append(authorName)
    elif len(authors) == 2:
        author1 = str(authors[0])
        author2 = str(authors[1])

        # Adding author 1 into our array
        newSoup = BeautifulSoup(author1, 'html.parser')
        authorName1 = newSoup.a.string
        authorList.append(authorName1)
        
        # Adding author 2 into our array
        newSoup = BeautifulSoup(author2, 'html.parser')
        authorName2 = newSoup.a.string
        authorList.append(authorName2)
    elif len(authors) == 3:
        author1 = str(authors[0])
        author2 = str(authors[1])
        author3 = str(authors[2])

        # Adding author 1 into our array
        newSoup = BeautifulSoup(author1, 'html.parser')
        authorName1 = newSoup.a.string
        authorList.append(authorName1)
        
        # Adding author 2 into our array
        newSoup = BeautifulSoup(author2, 'html.parser')
        authorName2 = newSoup.a.string
        authorList.append(authorName2)

        # Adding author 3 into our array
        newSoup = BeautifulSoup(author3, 'html.parser')
        authorName3 = newSoup.a.string
        authorList.append(authorName)

    # Saving the text of the article
    articleText = str(soup.find_all("p"))
    

    # Output of our information
    print("---------- Article Information ----------")
    print("SOURCE: " + siteName)
    print("TITLE: " + title)
    print("AUTHOR(S): ")
    printAuthors(authorList)
    # print("Text: " + articleText)


#### Running ####
articleInfo(URL)
