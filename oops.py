#class & object

class Student():
    name = "Aditya"
    
s1 = Student()
print(s1)
print(s1.name)

#second example

class car:
   colour = "blue"
   brand = "BMW"

car1 = car()
print(car1.colour)
print(car1.brand)

#constructor , __init__function

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = student("Aditya")
print(s1.name)

#second example

class student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = student("Aditya",97)
print(s1.name, s1.marks)

