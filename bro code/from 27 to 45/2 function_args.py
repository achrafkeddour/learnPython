"""
Arguments 
--------------------------------------
1. Positional Arguments
2. Default Arguments
3. Keyword Arguments
4. *args (Arbitrary Positional Arguments)
5. **kwargs (Arbitrary Keyword Arguments)
"""

# 1. Positional Arguments
def saying_hello(name, year_of_birth):
    year_of_birth = int(year_of_birth)
    age = 2025 - year_of_birth
    name = name.capitalize()  # Capitalize the name
    return f"Hello {name}, your age is {age}"

# 2. Default Arguments
import time

def count(end, start=0):
    for i in range(start, end + 1):
        print(i)
        time.sleep(0.3)
    print("DONE!")

count(10)  # Starts from 0 by default
count(10, 2)  # from 2 to 10

# 3. Keyword Arguments
count(start=3, end=10)  # Keyword args allow swapping order

# Example function using keyword arguments
def get_phone(country, operator, num):
    return f"{country}-{operator}-{num}"
print(get_phone(213, 7, 75202474))

# 4. *args (Arbitrary Positional Arguments)
def somme(*args):
    return sum(args)

print(somme(1, 2, 3))
print(somme(1, 2, 3, 4, 5, 6))

# Using *args to print multiple arguments
def naming(*args):
    for arg in args:
        print(arg,end=' ')

naming("Mr.", "Bro", "Code", "YouTube")
naming("Achraf", "Keddour")

# 5. **kwargs (Arbitrary Keyword Arguments)
def afficher_infos(*args, **kwargs):
    for k, v in kwargs.items():
        print(f"{k:^10} : {v:^10}")
    for arg in args:
        print(f"Autre argument : {arg}")
    
    # Accessing specific keyword arguments
    print(kwargs.get("school"))
    if "age" in kwargs:
        print(f"Age exists, it's {kwargs['age']}")

afficher_infos("Madrid", "Python", 2003, name="Achraf", age=22, school="ENPO")

# Example of merging dictionaries using **kwargs
def fusionner_dicts(dict1, **kwargs):
    dict1.update(kwargs)
    return dict1

dict1 = {"nom": "Mohamed",
         "age": 40}
info_to_add = {"school": "ESI",
               "birth": 1985}
print(fusionner_dicts(dict1, **info_to_add))
