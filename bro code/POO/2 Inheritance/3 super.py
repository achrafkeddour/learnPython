""" super() : a function used in a child class to call method from a parent class (superclass)
    allows us to extend the functionnality of the inherited methods (we will reuse them)"""
    
    
# ex 1 
class Parent:
    def greet(self):
        print("hello from parent")
        
class Child(Parent):
    def greet(self):
        super().greet() # calls the the greet of parent
        print("hello from child also")
        
        
child = Child()
child.greet() # hello from parent
              # hello from child also
              
              
# ex 2 
print("\n\nex 2 \n")
class Human:
    def __init__(self,name):
        self.name = name
        print(f"the name of the human is {self.name}")
        
class Man(Human):
    def __init__(self,name,age):
        super().__init__(name) # hadi __init__ ta3 Human
        self.age= age
        print(f"the age of the man is {self.age}")
        
        
man = Man("achraf",22)

