class Flyer:
    def fly(self):
        print("Duck is flying")

class Swimmer:
    def swim(self):
        print("Duck is swimming")

class Duck(Flyer,Swimmer):
    pass

duck = Duck()
duck.fly()
duck.swim()