# Name: Liu Eng Ann Joseph
# Email: kelpabc123@gmail.com
# Filename: course.py
# File: Contains class definitions for a course object




# Course object stores the information associated with a course
class course:
    
    ############ Constructor and  private/overloaded methods ############

    #Constructor for course object given string title and description
    def __init__(self, title, desc):
        titleArr = title.split(".")
        self.id = int(titleArr[0].strip())
        self.dept = titleArr[0].split(" ")[0]
        self.title = titleArr[1].strip() #includes units, TODO will figure out a way to parse/error check edge cases
        descBreakdown = desc.split("Prerequisites:")
        self.desc = descBreakdown[0].strip()
        self.prereq = descBreakdown[1].strip() #prerequisites will be parsed into array eventually, handled later TODO

    #Constructor for course object given list read from .csv file
    def __init__(self, list):
        self.id = list[0]
        self.dept = list[1]
        self.title = list[2]
        self.desc = list[3]
        self.prereq = list[4]

    #Overloaded string 
    def __str__(self):
        return f"{self.id}. {self.title}"


    

        