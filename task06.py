class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
        
    def deposit(self,deposit):
        self.__balance += deposit
        
    def withdraw(self,withdraw):
        self.__balance -= withdraw
        
    def get_balance(self):
        return self.__balance
    
acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())