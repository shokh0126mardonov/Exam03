class Account:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Not enough balance"


class SavingsAccount(Account):
    def __init__(self, balance=0, interest_rate=0.05):
        super().__init__(balance)   
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        return self.balance * self.interest_rate


class CheckingAccount(Account):
   
    pass



savings = SavingsAccount(1000, 0.1)  
print("Savings balance:", savings.balance)
print("Interest:", savings.calculate_interest())

checking = CheckingAccount(500)
checking.deposit(200)
checking.withdraw(100)
print("Checking balance:", checking.balance)
