# BankAccount class
class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to Stanbic bank")

# Function to deposit amount
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

# Function to withdraw the amount
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")

# Function to display the amount
    def display(self):
        print("\n Net Available Balance =", self.balance)

# creating an object of class
s = Bank_Account()

# Calling functions with the class object
s.deposit()
s.withdraw()
s.display()