from abc import ABC,abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay():
        pass

class PayPalPayment(Payment):
        
    def pay(self,money):
        print(f"Paid {money} using PayPal")

class CardPayment(Payment):
        
    def pay(self,money):
        print(f"Paid {money} using Card")
        
p1 = PayPalPayment()
p2 = CardPayment()
p1.pay(100)
p2.pay(200)