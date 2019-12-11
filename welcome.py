from tabulate import tabulate

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Student(Person):
    def __init__(self, fname, lname, uni_name, graduation_year):
        super().__init__(fname, lname)
        self.uni_name = uni_name
        self.graduation_year = graduation_year
        
    def details(self):
        print(tabulate([[self.fname, self.lname, self.uni_name, self.graduation_year]], headers=["First Name", "Last Name", "University", "Graduation Year"]))
       # print("Full Name:", self.fname, self.lname)
       # print("University name:", self.uni_name)
       # print("Graduation Year:", self.graduation_year)
 
student1 = Student("Riya", "Shah", "Saint Peter's University", 2019)
student1.details()
