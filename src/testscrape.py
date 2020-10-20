#this is for testing, an internal testbench to verify implemented features

from bs4 import BeautifulSoup
from course import MyCourse
import requests
import csv
import cscraper

cscraper.updateCSV()
courses = cscraper.findCoursebyID("MaTh 170")
for course in courses:
    course.printCourse()
courses = cscraper.findCoursebyDesc("experiment")
for course in courses:
    print(course)
courses = cscraper.findCoursebyTitle("Materials")
for course in courses:
    print(course)
#url = "https://ucsd.edu/catalog/front/courses.html"
#req = requests.get(url)
#soup = BeautifulSoup(req.text, "lxml")
#for tag in soup.findAll("a", string="courses"):
    #print(tag.get('href'))
#for tag in soup.findAll('p','course-name'):
#    print(tag.text)
#    print(tag.find_next('p','course-descriptions').text