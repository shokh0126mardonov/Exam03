class Cart:
    def __init__(self):
        self.total = []
        
    def add_item(self,name,price):
        self.total.append({"name":name,"price":price})
    
    def get_total(self):
        s=0
        for i in self.total:
            s += i['price']
            
        return s
        
cart = Cart()
cart.add_item("Laptop", 2000)
cart.add_item("Mouse", 100)
print(cart.get_total())