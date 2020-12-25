#parentclass
class Customer():
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def show(self):
        print("Name :", self.name)
        print("Number :", self.number)

#chidclass
class Dapur():
    def __init__(self, name, number):
        super().__init__(name, number)
        self.balance = 0
    
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Total :", self.balance)

    #def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print 