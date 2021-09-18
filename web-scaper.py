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
# URL = 'https://www.nytimes.com/2021/09/18/world/covid-trash-recycling.html?searchResultPosition=1'
URL = 'https://www.nytimes.com/live/2021/09/18/world/covid-delta-variant-vaccine'
# URL = 'https://www.nytimes.com/2021/09/18/opinion/sunday/manchin-vote-voting-bill.html'
# URL = 'https://www.usatoday.com/story/news/politics/2021/09/17/justice-j-6-organizer-ex-trump-staffer-election-fraud-promoter/8379295002/'
# URL = 'https://www.usatoday.com/story/tech/reviewedcom/2018/11/07/the-20-best-gifts-for-mom-that-shell-actually-want/38368663/'
# URL = 'https://www.usatoday.com/story/news/nation/2021/09/18/gabby-petito-still-not-found-authorities-searching-brian-laundrie/8397320002/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Global variable used for our author(s) and text
authorList = []
textArray = []

# Printing the source name (works abstractly)
arrayWeb = URL.split('/')
siteName = arrayWeb[2]

def printList(authorlist):
    # TODO: Make sure you get rid of the random 'u' in front of each string element
    # print(authorList)
    for author in authorList:
        print("\t" + "* "  + author)

def printText(texts):
    # TODO: Make sure you get rid of the random 'u' in front of each string element
    for text in texts:
        if text.encode('utf-8') is not None:
            print(text.encode('utf-8'))

def articleInfo(url):
    # Saving the title
    title = soup.title.string

    if siteName == "www.nytimes.com":
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

        # Extracting article text
        texts = soup.find_all(class_='css-axufdj evys1bk0')
        # print(texts)
        for text in texts:
            newSoup = BeautifulSoup(text.encode('utf-8'), 'html.parser')
            tag = newSoup.p           
            textArray.append(tag.string)

    elif siteName == "www.usatoday.com":
        # Saving the author(s)
        authors = soup.find_all(class_='gnt_ar_by_a gnt_ar_by_a__fi')

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

        # Extracting article text
        # texts = soup.find_all(class_='gnt_ar_b_p')
        # # print("Text is shown...")
        # # print(texts)
        # textArray = []
        # for text in texts:
        #     print(str(text))
        #     newSoup = BeautifulSoup(text, 'html.parser')
        #     textArray.append(newSoup.p.string)
            
            

    # Output of our information
    print("---------- Article Information ----------")
    print("SOURCE: " + siteName)
    print("TITLE: " + title)
    print("AUTHOR(S): (Currently multiple authors aren't supported)")
    if len(authorList) == 0:
        print("Unfortunately, we weren't able to pull any author names")
    else:
        printList(authorList)
    print("Text: ")
    print(textArray)
    


#### Running ####
articleInfo(URL)
