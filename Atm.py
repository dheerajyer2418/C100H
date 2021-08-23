class Atm(object):
    def __init__(self, name, age, gender,cardNo,cardPin):
        self.name = name
        self.age = age
        self.gender = gender
        self.cardNo = cardNo
        self.cardPin = cardPin
        self.balance= 1000000
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("gender:",self.gender) 
        print("cardNo:",self.cardNo) 
        print("cardPin:",self.cardPin) 
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('Deposit of rupees ',str(amount)," successful")
    def withdraw(self,amount):
        self.balance=self.balance-amount
        print('Withdrawal of rupees ',str(amount)," successful")
    def balanceEnquiry(self):
        print("Your total balance is:",str(self.balance))

Dheeraj=Atm("Dheeraj","15","male","1234567890","1234")
Dheeraj.display()
Dheeraj.deposit(1000000)
Dheeraj.withdraw(500000)
Dheeraj.balanceEnquiry()