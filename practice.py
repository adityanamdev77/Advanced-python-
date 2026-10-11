#print numbers from 1 to 100 

i = 1
while i<= 100:
   print(i)
   i += 1
   
   
#print numbers from 100 to 1

i = 100
while i >= 1:
    print(i)
    i -= 1
   
# print the multiplication table of a number n.

i = 1
n = int(input("enter number : "))
while i <= 10:
    print(n*i)
    i += 1
    
#print the element of the following list using a loop:

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(num):
    print(num[idx])
    idx += 1 
    
#search for a number x in this tuple using loop:

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0 
while i < len(num):
    if(num[i] == x):
        print("found at idx", i)
    else:
        print("finding", i)
        
    i += 1
    
#print the element of the following list using a loop:

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in num:
    print(el)
    
#search for a umber x in this tuple using loop:

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,49)

x = 49

idx = 0
for el in num:
    if(el == x):
        print("number found at idx", idx)
    idx += 1
    
#range
#print numbers from 1 to 100.
for i in range (1, 101):
    print(i)
    
#print the multiplication table of a number n.

n = int(input("enter number : "))
for i in range(1, 11):
    print(n*i)
    
#WAP  to find the sum of first numbers.(using while)

n = 5

sum = 0
for i in range(1, n+1):
    sum += i
print("sum of total numbers:", sum)

#WAP to find the factorial of first n numbers. (using for loop

n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial of", n, "is:", fact)