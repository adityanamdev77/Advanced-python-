class student:
    college_name = "ABC college"#class attributes 

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = student("Aditya",97)
print(s1.name, s1.marks)
print(s1.college_name)

#methods

class student:
    college_name = "Sage university"#class attributes 

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("Welcome to sage university", self.name)
    
    def get_marks(self):
        return self.marks
    
s1 = student("Aditya",97)
print(s1.name, s1.marks)
print(s1.college_name)
s1.welcome()

#create a student class that takes name & marks of 3 subject as arguments in constructor. then create a method to print the average.

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def hello(self):
        print("hello")
        
    def get_avg(self):
         sum = 0
         for val in self.marks:
             sum += val
             print("hi", self.name, "your average is", sum/3)
    
s1 = student("Aditya",[97,98,99])
s1.get_avg()
s1