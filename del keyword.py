class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("aditya")
print(s1.name)
del s1.name
print(s1.name)

#private attributes & methods - attributes and methods which are not accessible outside the class

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass87654 return       
    def reset_pass(self):
        print(self.__acc_pass)
        
    acc1 = Account(12345, "aditya@123")
    
    print(acc1.acc_no)
    print(acc1.reset_pass())
    
#second example

class person:
    __name = "aditya"
    
    def __hello(self):
        print("hello person!")
        
    def welcome(self):
        self.__hello()
        
p1 = person()