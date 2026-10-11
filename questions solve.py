#WAP to print length of a list.(list is the parameter)

from operator import le


cities = ["Pune", "Mumbai", "Delhi", "Bangalore", "Chennai"]
heroes = ["Superman", "Batman", "Spiderman", "Ironman"]

def print_list_len(list):
    print(len(list))
    
print_list_len(cities)
print_list_len(heroes)

#WAP to print the elements of a list in a single line.(list is the parameter)

cities = ["Pune", "Mumbai", "Delhi", "Bangalore", "Chennai"]
heroes = ["Superman", "Batman", "Spiderman", "Ironman"]

def print_list_len(list):
    print(len(list))
    
def print_list(list):
    for item in list:
        print(item, end=" ")
    print()  # Print a newline at the end
    

#WAF to find the factorial of n. (n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
    
cal_fact(5)

#WAF to convert USD to INR 

def converter(usd_val):
    inr_val = usd_val * 90
    print(usd_val, "USD =", inr_val, "INR")
    
converter(10)

# write a recursive function to calculate the sum of first n natural numbers.

def calc_sum(n):
    if(n == 0 ):
        return 0
    return n + calc_sum(n-1)+n

sum =  calc_sum(10)
print(sum)

#write a recursion function to print all elements in a list.
#hint : use list & index as parameter 

def print_list(list, idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    print_list(list, idx+1)
    
cities = ["Pune", "Mumbai", "Delhi", "Bangalore", "Chennai"]
print_list(cities)