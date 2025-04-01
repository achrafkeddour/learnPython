"""__init__ Method 
__init__ is a special method in Python called the constructor. 
It is automatically called when you create a new object from a class. 
Its purpose is to initialize the object's attributes.
"""

""" What is self?
self represents the instance of the class.

It allows us to access and modify attributes specific to that object.

Every method inside a class must include self as the first parameter."""


from thecar import Car 
    
mycar = Car("BMW",2020,"blue",True)
print(f"nbdaw bla couleur , li hia '{mycar.color}'",end='\n\n')
print(mycar.get_info())

print(mycar.repaint("white"))
print()
print(mycar.get_info())
print()
print(mycar.get_price())
mycar.change_price(5000)
print(mycar.get_price())


import time
""" classes variables and instances variables """
print("\n\n\n classes variables and instances variables ", end='\n\n')

class Student:
    class_year = 2025       #classes variable (shared among all instances)
    num_students = 0        #classes variable
    
    def __init__(self,name,age):
        self.name = name  # Instance variable (unique to each instance)
        self.age = age    # Instance variable 
        Student.num_students += 1 
        """ à chaque fois je definis une nouvelle instance de la classe Student , 
        la variable de classe num_students se change ! """



student1 = Student("achraf", 22)
print(f"we are in {Student.class_year} ")

print(f"num of students is {Student.num_students}")

print("adding another student...")
time.sleep(1)
student2 = Student("bro code",23)
print(f"num of students is {Student.num_students}")

print("adding another student...")
time.sleep(1)
student3 = Student("asus",40)
print(f"num of students is {Student.num_students}")

print(f"our students are : {student1.name} and {student2.name} and {student3.name}")
