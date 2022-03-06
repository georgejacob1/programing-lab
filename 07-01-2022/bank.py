class Bank:
    def __init__(self,acno,n,t,b):
        self.acc = acno
        self.name = n
        self.type = t
        self.bal = b
    def deposit(self,d):
        self.bal += d
    def withdraw(self,w):
        if(self.bal < w):
            print("Insufficient balance")
        else:
            self.bal -= w
    def disp(self):
        print("Name of Customer:",self.name)
        print("Account type:",self.type)
        print("Balance:",self.bal)
acno = int(input("Enter your account number: "))
n = input("Enter your name: ")
t = input("Enter your account type: ")
b = int(input("Enter your account balance: "))
bnk = Bank(acno,n,t,b)
d = int(input("Enter the amount to deposit: "))
bnk.deposit(d)
w = int(input("Enter the amount to withdraw: "))
bnk.withdraw(w)
bnk.disp()