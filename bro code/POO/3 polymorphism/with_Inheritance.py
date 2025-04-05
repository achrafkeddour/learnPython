""" Polymorphism : is a greek word that means 'to have many forms or faces' 
Poly = many
morphism = form

TWO WAYS TO ACHIEVE POLYMORPHISM
1. Inheritance = When a subclass overrides a method from its superclass, allowing different behaviors for the same method name in different classes.
2. Duck typing = an object is valid while it has the required behavior/methods, no inheritance required , meaning if it "quacks like a duck and walks like a duck," it's treated as a duck.

""" 

# Polymorphism using Inheritance
# When a child class overrides a method from its parent class, we achieve polymorphism.

class human:
    def speak(self):
        return "each human has what to say"
    
    
class arabic(human):
    def __init__(self,year):
        self.year= year
        
    def speak(self):
        return f"nahnou fi 3am {self.year}"
        
class english(human):
    def __init__(self,y):
        self.y = y
        
    def speak(self):
        return f"we are in the year {self.y}"
    
def print_year(entity: human): # il faut une classe qui herite 'human'
    print(f"we say : {entity.speak()}")
    
    
ahmed = arabic("1446")
john = english("2025")

print_year(ahmed)
print_year(john)
