class Temperature:
    def __init__(self,temperatura):
        self.temperatura = temperatura
        
    @property
    def celsius(self):
        return self.temperatura * 9/5 +32
    
    @property
    def fahrenheit(self):
        return (self.temperatura - 32) * 5/9
    
t = Temperature(0)
print(t.celsius)
print(t.fahrenheit)
