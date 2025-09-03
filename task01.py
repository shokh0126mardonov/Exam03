class Car:
    def __init__(self,Car,model,year):
        self.Car = Car
        self.model = model
        self.year = year
        
    def get_info(self):
        return f"{self.Car} {self.model} ({self.year})"
    
car = Car("BMW", "X5", 2020)
print(car.get_info())