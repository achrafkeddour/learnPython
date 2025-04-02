# multiple inheritance & multilevel inheritance

class Animal:
    def __init__(self,name):
        self.name = name
    def is_animal(self):
        print(f"{self.name} is an animal\n ")


class Prey(Animal): # Prey inherit methods of Animal class (__init__ and is_animal )
    def flee(self):
        print(f"{self.name} is fleeing")
        
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting ")
        
class Rabbit(Prey): # this means we inherit only flee method (not hunt) -- wbayna we inherit les methods ta3 Animal tani (multilevel inheritance)
    pass

class Hawk(Predator): # this means we inherit only hunt method (not flee)
    pass 

class Fish(Prey,Predator): # inherit method of to classes
    pass


rabbit1 = Rabbit("my rabbit")
rabbit1.flee() # my rabbit is fleeing
# rabbit1.hunt() # error because we didnt inherit it 
rabbit1.is_animal()

hawk1 = Hawk("myhawk")
hawk1.hunt() # myhawk is hunting
# hank1.flee() # error
hawk1.is_animal()

fish1 = Fish("my fish")
fish1.flee() # my fish is fleeing
fish1.hunt() # my fish is hunting
fish1.is_animal()
