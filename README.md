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

### 7. Classmethod & Staticmethod (updated)

**Task:** `StringTools` classida:

* `is_palindrome(text)` static methodi yozing
* `from_sentence("I love Python")` classmethod orqali obyekt yarating va so‘zlar ro‘yxatini saqlang.

**Input:**

```python
print(StringTools.is_palindrome("level"))
st = StringTools.from_sentence("I love Python")
print(st.words)
```

**Output:**

```
True
['I', 'love', 'Python']
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

### 14. Cart class

**Task:** `Cart` classini yozing.

* `add_item(name, price)` metodida mahsulot qo‘shilsin
* `get_total()` umumiy narxni hisoblasin

**Input:**

```python
cart = Cart()
cart.add_item("Laptop", 2000)
cart.add_item("Mouse", 100)
print(cart.get_total())
```

**Output:**

```
2100
```

---

### 15. TodoList class

**Task:** `TodoList` classini yozing.

* `add_task(task)` metodida vazifa qo‘shilsin
* `show_tasks()` metodida barcha vazifalar chiqsin

**Input:**

```python
todo = TodoList()
todo.add_task("Do homework")
todo.add_task("Clean room")
todo.show_tasks()
```

**Output:**

```
1. Do homework
2. Clean room
```

---

### 16. Bank Account – Inheritance (updated & clear)

**Task:** `Account` nomli asosiy class yozing.

* Unda `balance` atributi va `deposit(amount)` hamda `withdraw(amount)` metodlari bo‘lsin.

So‘ngra undan ikkita class hosil qiling:

1. **SavingsAccount**

   * `interest_rate` atributiga ega bo‘lsin.
   * `calculate_interest()` metodi balans bo‘yicha foiz hisoblab qaytarsin (`balance * interest_rate`).

2. **CheckingAccount**

   * Oddiy `deposit()` va `withdraw()` metodlari ishlasin (foizsiz).

---

**Input:**

```python
s = SavingsAccount(1000, 0.05)  # 5% foiz stavkasi
s.deposit(500)                  # balansga qo‘shildi
print(s.calculate_interest())
```

**Output:**

```
75.0
```

---

📌 Ya’ni:

* Avval `Account` → umumiy bank hisob
* Keyin `SavingsAccount` → foizli hisob
* `CheckingAccount` → oddiy hisob

---

### 17. Session class

**Task:** `Session` classini yozing.

* `login(username)` metodida foydalanuvchi tizimga kiradi
* `logout()` metodida tizimdan chiqadi

**Input:**

```python
s = Session()
s.login("Ali")
s.logout()
```

**Output:**

```
Ali logged in
Ali logged out
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
