#abstraction , #inheritence, #encapsulation, #polymorphism
#hiding the implementation details and showing only functionality to the user


class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("car started")
        
s1 = car()
s1.start()

#create account class with 2 attributes - balance & amount no.
#create method for debit,credit & ptinting the balance 

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("Total balance = ", self.get_balance())
    
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("Total balance = ", self.get_balance())
        
    def get_balance(self):
        return self.balance
    
acc1 = Account(1000, 123456)
acc1.debit(500)
acc1.credit(1000)
acc1.get_balance()
   
   
#inheritance - when a class inherits the properties of another 

class Car:
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stopped.")

class Toyotacar(Car):
    def __init__(self,name):
        self.name = name
        
car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")

print(car1.start())      

#Class methods

class person:
    name = "aditya"
    
    @classmethod
    def changename(obj, newname):
        self.__class__.name = "aditya"
        
p1 = person()
p1.changename("aditya namdev")
print(p1.name)
print(person.name)

#pr