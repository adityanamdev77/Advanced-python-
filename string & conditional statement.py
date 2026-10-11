str =  "this is string\nwe are creating in python."
print(str)

#stringg add

str1 = "aditya"
str2 = "namdev"
final_str = str1+str2
print(final_str)

#length

str1 = "aditya"
len1 = len(str1)
print(len1)

str2 = "namdev"
len2 = len(str2)
print(len2)

final_str=str1+str2
print(final_str)

#indexing

str="aditya namdev"
ch = str[2]
print(ch)

#slicing

str1 ="aditya namdev"
print(str1[0:6])

#string function

str = "aditya namdev"
print(str.endswith("dev"))

age = 24

if age >= 18:
    print("can vote")
    print("can drive")
    
    
light = "yellow"

if light == "red":
    print("stop")
elif light == "yellow":
    print("wait")
else: 
     print("light is broken")
     

marks = int(input("enter student marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
    
print("grade of the student ->", grade)


# WaP to check if a number entered by the user is odd or even.

num = int(input("enter number: "))

rem = num % 2

if rem == 0:
    print("number is even") 
else:
    print("number is odd")
    
#WAP to find the gretest of 3 numbers entered by the user.

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a >= b and a >= c:
    print("first number is greatest")
elif b >= a and b >= c:
    print("second number is greatest")
else:
    print("third number is greatest")

# WAP to check if a number entered by the user is a multiple of 7 or not.    
x = int(input("enter number:"))

if (x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple of 7")print("print("")")