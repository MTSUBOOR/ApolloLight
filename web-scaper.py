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


# GME stock
URL = 'https://finance.yahoo.com/quote/GME?.tsrc=applewf'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# AMC stock
URL2 = 'https://finance.yahoo.com/quote/AMC?p=AMC&.tsrc=fin-srch'
page2 = requests.get(URL2)
soup2 = BeautifulSoup(page.content, 'html.parser')

# BB stock
URL3 = 'https://finance.yahoo.com/quote/BB?p=BB&.tsrc=fin-srch'
page3 = requests.get(URL3)
soup3 = BeautifulSoup(page.content, 'html.parser')

URL4 = 'https://nationalpost.com/news/politics/election-2021/canadians-find-trudeau-angry-and-pretty-much-in-unison-the-campaign-divisive-poll'
page4 = requests.get(URL4)
soup4 = BeautifulSoup(page.content, 'html.parser')


def stockInfoExtract(url, stockNum):
    URL = url
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Printing the source name
    arrayWeb = URL.split('/')
    arraySite = arrayWeb[2].split('.')
    siteName = arraySite[1] + " " + arraySite[0]

    # Saving the Ticker
    title = str(soup.find(class_='D(ib) Fz(18px)'))
    titlePt1 = title.split(">", 1)
    titlePt2 = titlePt1[1].split("<")
    finalTitle = titlePt2[0]

    # Saving the price value
    price = soup.find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
    priceStr = str(price)
    pricePt1 = priceStr.split(">", 1)
    pricePt2 = pricePt1[1].split("<")
    finalPrice = pricePt2[0]

    # Saving the after hour price value
    """
    afterPrice = str(soup.find(class_="C($primaryColor) Fz(24px) Fw(b)"))
    afterPricePt1 = afterPrice.split(">", 1)
    afterPricePt2 = afterPricePt1[1].split("<")
    finalAfterPrice = afterPricePt2[0]
    """

    # Output of our information
    print("########### Stock " + str(stockNum) + " ###########")
    print("SOURCE: " + siteName)
    print("COMPANY + TICKER: " + finalTitle)
    print("PRICE: " + "$" + finalPrice)
    # print("AFTER HRS PRICE: " + "$" + finalAfterPrice)
    print("\n")


def articleInfo(url, stockNum):
    URL = url
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Printing the source name (works abstractly)
    arrayWeb = URL.split('/')
    siteName = arrayWeb[2]

    # Saving the title (NEEDS EDITS HOMEBOY)
    title = str(soup.find(class_='article-title'))
    # print(title)
    titlePt1 = title.split(">", 1)
    # print(titlePt1)
    titlePt2 = titlePt1[1].split("<")
    # print(titlePt2)
    finalTitle = titlePt2[0]
    #print(finalTitle)

    # Saving the title (NEEDS EDITS HOMEBOY)
    author = str(soup.find(class_='published-by__author'))
    # print(title)
    authorPt1 = author.split(">", 1)
    # print(titlePt1)
    authorPt2 = authorPt1[1].split("<")
    # print(titlePt2)
    finalAuthor = authorPt2[0]
    #print(finalTitle)

    # Saving the text of the article
    articleText = str(soup.find_all("p"))
    

    # Output of our information
    print("---------- Article Information ----------")
    print("SOURCE: " + siteName)
    print("TITLE: " + finalTitle)
    print("AUTHOR: " + finalAuthor)
    # print("Text: " + articleText)



#### Welcome Note ####
print("####### Welcome to Stonk Viewer #######\n")
stockNum = 1
stockInfoExtract(URL, stockNum)
stockNum += 1
stockInfoExtract(URL2, stockNum)
stockNum += 1
stockInfoExtract(URL3, stockNum)
stockNum += 1
articleInfo(URL4, stockNum)

# Adding GUI Stuff
# Creating our root
# root = tk.Tk()

# Updating the look of our canvas
# canvas = tk.Canvas(root, height=700, width=700, bg="#04407d")
# Attaching our canvas changes
# canvas.pack()

# Creating our search button
# search = tk.Button(root, text="Search", padx=10, pady=5, fg="white", bg="#04407d", command=stockInfoExtract(URL, stockNum))
# search.pack()

# Running our GUI
# root.mainloop()
