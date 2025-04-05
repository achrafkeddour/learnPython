# If an object can do what we need, we just use it—no need to check its class or inheritance tree
# No inheritance, no shared parent class. We're just saying: li ydir hadi la methode ytfadel 
    
class arabic:
    def __init__(self,year):
        self.year= year
        
    def speak(self):
        return f"nahnou fi 3am {self.year}"
        
class english:
    def __init__(self,y):
        self.y = y
        
    def speak(self):
        return f"we are in the year {self.y}"
    
def print_year(entity): # n'importe classe , lmohim tdir la methode speak()
    print(f"we say : {entity.speak()}") # nzidou try/except khir 
    
    
ahmed = arabic("1446")
john = english("2025")

print_year(ahmed)
print_year(john)
