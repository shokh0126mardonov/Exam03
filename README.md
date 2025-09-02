# 📝 Exam 03 – Python OOP

---

### 1. Class yaratish

**Task:** `Car` nomli class yozing. Unda `brand`, `model`, `year` atributlari bo‘lsin va obyekt haqida ma’lumot qaytaradigan `get_info()` methodini yozing.

**Input:**

```python
car = Car("BMW", "X5", 2020)
print(car.get_info())
```

**Output:**

```
BMW X5 (2020)
```

---

### 2. Constructor

**Task:** `Student` class yarating. `introduce()` methodi orqali talaba o‘zini tanishtirsin.

**Input:**

```python
s = Student("Ali", 20, 2)
print(s.introduce())
```

**Output:**

```
My name is Ali, I am 20 years old, studying in 2nd course.
```

---

### 3. Inheritance – asosiy

**Task:** `Dog` classi `Animal` dan meros olsin va `bark()` methodiga ega bo‘lsin.

**Input:**

```python
d = Dog("Rex")
print(d.name)
d.bark()
```

**Output:**

```
Rex
Woof! Woof!
```

---

### 4. Multiple Inheritance

**Task:** `Duck` classini `Flyer` va `Swimmer` dan meros oling.

**Input:**

```python
duck = Duck()
duck.fly()
duck.swim()
```

**Output:**

```
Duck is flying
Duck is swimming
```

---

### 5. Polymorphism

**Task:** `Shape` abstract classidan `Circle` va `Rectangle` classlarini yarating.

**Input:**

```python
c = Circle(5)
r = Rectangle(4, 6)
print(c.area())
print(r.area())
```

**Output:**

```
78.5
24
```

---

### 6. Encapsulation

**Task:** `BankAccount` classida balans private bo‘lsin.

**Input:**

```python
acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())
```

**Output:**

```
120
```

---

### 7. Classmethod & Staticmethod

**Task:** `MathTools` classida factorial va string parsing yozing.

**Input:**

```python
print(MathTools.factorial(5))
mt = MathTools.from_string("5,6,7")
print(mt.numbers)
```

**Output:**

```
120
[5, 6, 7]
```

---

### 8. Magic Methods

**Task:** `Vector` classida `__add__` metodini overload qiling.

**Input:**

```python
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)
```

**Output:**

```
Vector(6, 8)
```

---

### 9. Property

**Task:** `Temperature` classida `celsius` va `fahrenheit` property bo‘lsin.

**Input:**

```python
t = Temperature(0)
print(t.celsius)
print(t.fahrenheit)
```

**Output:**

```
0
32.0
```

---

### 10. Inheritance + super()

**Task:** `Employee` classini `Person` dan meros oling.

**Input:**

```python
e = Employee("Hasan", 25, "Google")
print(e.get_info())
```

**Output:**

```
Hasan, 25 years old, works at Google
```

---

### 11. Composition

**Task:** `Book` classida `Author` obyektidan foydalaning.

**Input:**

```python
a = Author("Alisher Navoiy")
b = Book("Xamsa", a)
print(b.get_info())
```

**Output:**

```
Book: Xamsa, Author: Alisher Navoiy
```

---

### 12. Abstract Base Class

**Task:** `Vehicle` abstract classini yarating.

**Input:**

```python
car = Car()
bike = Bike()
car.start_engine()
bike.start_engine()
```

**Output:**

```
Car engine started
Bike engine started
```

---

### 13. Interface-like Design

**Task:** `Payment` abstract classida `pay()` methodini implement qiling.

**Input:**

```python
p1 = PayPalPayment()
p2 = CardPayment()
p1.pay(100)
p2.pay(200)
```

**Output:**

```
Paid 100 using PayPal
Paid 200 using Card
```

---

### 14. Singleton Pattern

**Task:** `Logger` faqat bitta obyekt yaratsin.

**Input:**

```python
l1 = Logger()
l2 = Logger()
print(l1 is l2)
```

**Output:**

```
True
```

---

### 15. **str** vs **repr**

**Task:** `User` classida ikkalasini yozing.

**Input:**

```python
u = User("Ali", 25)
print(str(u))
print(repr(u))
```

**Output:**

```
User: Ali, Age: 25
User('Ali', 25)
```

---

### 16. Inheritance Chain

**Task:** `LivingThing → Animal → Mammal → Human`.

**Input:**

```python
h = Human()
h.breathe()
h.eat()
h.walk()
h.speak()
```

**Output:**

```
Breathing...
Eating...
Walking...
Speaking...
```

---

### 17. Destructor

**Task:** `FileHandler` classida fayl ochilib yopilsin.

**Input:**

```python
f = FileHandler("test.txt")
del f
```

**Output (terminal log):**

```
File opened
File closed
```

---

### 18. Operator Overloading

**Task:** `Time` classida `__lt__` metodini yozing.

**Input:**

```python
t1 = Time(10, 30)
t2 = Time(12, 15)
print(t1 < t2)
```

**Output:**

```
True
```

---

### 19. Mixins

**Task:** `JsonMixin` obyektni JSON ga aylantirsin.

**Input:**

```python
p = Product("Laptop", 1500)
print(p.to_json())
```

**Output:**

```
{"name": "Laptop", "price": 1500}
```

---

### 20. Real Project Mini-task

**Task:** `Library` system yozing.

**Input:**

```python
lib = Library()
lib.add_book("1984", "George Orwell")
lib.add_book("Xamsa", "Alisher Navoiy")

print(lib.borrow_book("1984"))
print(lib.borrow_book("1984"))
print(lib.return_book("1984"))
```

**Output:**

```
You borrowed '1984'
Sorry, '1984' is not available
You returned '1984'
```
