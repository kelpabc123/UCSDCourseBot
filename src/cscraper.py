# Name: Liu Eng Ann Joseph
# Email: kelpabc123@gmail.com
# Filename: cscraper.py
# File: Scrapes

from bs4 import BeautifulSoup
import course 
import csv
import requests

#scrapes the UCSD courses page and updates all files, taking a strList file containing
def updateCSV():
    masterURL = "https://ucsd.edu/catalog/front/courses.html" # The course masterlist
    mreq = requests.get(masterURL)
    master = BeautifulSoup(req.text, "lxml")
    headURL = "https://ucsd.edu/catalog/"
    for link in master.findAll("a", string="courses"):
        link = link[2:]
        link = headURL + link
        course = requests.get(link)
        