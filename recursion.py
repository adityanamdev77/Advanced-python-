#recuirsion 

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    
show(5)

#satck call function in recursion 

def show(n):
    if(n == 0):
        return 
    print(n)
    show(n-1)
    print("END")
    
show(5)

#factorial of n using recursion

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(5))