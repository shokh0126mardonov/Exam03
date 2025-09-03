class Person:
    def __init__(self,name,age,work):
        self.name = name
        self.age = age
        self.work = work

class Employee(Person):
    def get_info(self):
       return f"{self.name}, {self.age} years old, works at {self.work}"
        
        
e = Employee("Hasan", 25, "Google")
print(e.get_info())