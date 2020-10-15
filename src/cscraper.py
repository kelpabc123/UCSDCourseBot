# Name: Liu Eng Ann Joseph
# Email: kelpabc123@gmail.com
# Filename: cscraper.py
# File: Scrapes

from bs4 import BeautifulSoup
from course import MyCourse
import csv
import requests

#scrapes the UCSD courses page and updates all files, taking a strList file containing
def updateCSV():
    masterURL = "https://ucsd.edu/catalog/front/courses.html" # The course masterlist
    mreq = requests.get(masterURL)
    master = BeautifulSoup(mreq.text, "lxml")
    headURL = "https://ucsd.edu/catalog/"
    csvFile = "data/courses.csv"
    with open(csvFile,"w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for link in master.findAll("a", string="courses", multi_valued_attributes=None):
            linkURL = link['href']
            linkURL = linkURL[2:]
            linkURL = headURL + linkURL
            course = requests.get(linkURL)
            data = BeautifulSoup(course.text, "lxml")
            for courseTag in data.findAll("p","course-name"):
                title = courseTag.text
                desc = courseTag.find_next("p").text
                c = MyCourse( title , desc )
                c.write(writer)
