#functions

def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum

calc_sum(5,10) 

#more lines of code

calc_sum(12,14)

#function defination 
def calc_sum(a, b):#parameter
    return a + b

sum = calc_sum(178,222)#function call ; arguments
print(sum)

def print_hello(name):
    print ("Hello", name)

print_hello("Alice")
print_hello("Bob")
print_hello("Charlie")

#average of three numbers   

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    return avg

result = calc_avg(98, 97, 85)
print(result)

print("adityua namdev", end="$") #sep = ""
print("artificial intelligence")#end = "/n"

cities = ["Pune", "Mumbai", "Delhi", "Bangalore", "Chennai"]
heroes = ["Superman", "Batman", "Spiderman", "Ironman"]

def print_list_len(list):
    print(len(list))
    
def print_list(list):
    for item in list:
        print(item, end=" ")
    print()  # Print a newline at the end

