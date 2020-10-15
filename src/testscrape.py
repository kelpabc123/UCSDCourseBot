#this is for testing, an internal testbench to verify implemented features

from bs4 import BeautifulSoup
import requests
import csv
import cscraper

cscraper.updateCSV()
#url = "https://ucsd.edu/catalog/front/courses.html"
#req = requests.get(url)
#soup = BeautifulSoup(req.text, "lxml")
#for tag in soup.findAll("a", string="courses"):
    #print(tag.get('href'))
#for tag in soup.findAll('p','course-name'):
#    print(tag.text)
#    print(tag.find_next('p','course-descriptions').text