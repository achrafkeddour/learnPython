class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating..")
        
    def sleep(self):
        print(f"{self.name} is sleeping..")
        
class Cat(Animal):
    def speak(self):
        print("meow !")

class Dog(Animal):
    def speak(self):
        print("woof !")
        
class Mouse(Animal):
    pass

mouse1 = Mouse("jerry")
mouse1.eat() # jerry is eating..

cat1 = Cat("TOM")
cat1.sleep() # TOM is sleeping..

dog1 = Dog("scooby")
dog1.speak() # woof !
