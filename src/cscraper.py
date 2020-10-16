# Name: Liu Eng Ann Joseph
# Email: kelpabc123@gmail.com
# Filename: cscraper.py
# File: Scrapes

from bs4 import BeautifulSoup
from course import MyCourse
import csv
import requests

csvFile = "data/courses.csv"
#scrapes the UCSD courses page and updates all files, taking a strList file containing
def updateCSV():
    masterURL = "https://ucsd.edu/catalog/front/courses.html" # The course masterlist
    mreq = requests.get(masterURL)
    master = BeautifulSoup(mreq.text, "lxml")
    headURL = "https://ucsd.edu/catalog/"
    with open(csvFile,"w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for link in master.findAll("a", string="courses", multi_valued_attributes=None):
            linkURL = link['href']
            linkURL = linkURL[2:]
            linkURL = headURL + linkURL
            course = requests.get(linkURL)
            data = BeautifulSoup(course.text, "lxml")
            for courseTag in data.findAll("p","course-name"):
                title = courseTag.text.strip()
                title = " ".join(title.split()) #to fix formatting issues
                desc = courseTag.find_next("p").text
                c = MyCourse( title , desc, [], False )
                c.write(writer)

# reads the scraped CSV and returns a list of course objects associated with the search param
def findCoursebyID(id):
    with open(csvFile, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        id = id.upper()
        courseList = []
        for row in reader:
            if row[0].find(id)!= -1:
                courseList.append(MyCourse("","",row,True))
    return courseList

# takes a description, and returns a list of all courses with similar matching descriptions
def findCoursebyDesc(desc):
    with open(csvFile, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        desc = desc.lower()
        courseList = []
        for row in reader:
            if row[3].lower().find(desc)!= -1:
                courseList.append(MyCourse("","",row,True))
    return courseList

# takes a title, and outputs all courses with similar matching description
def findCoursebyTitle(title):
    with open(csvFile, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        desc = title.lower()
        courseList = []
        for row in reader:
            if row[2].lower().find(desc)!= -1:
                courseList.append(MyCourse("","",row, True))
    return courseList

