import random as rd

# رقم عشواي بين 0 و 1
print(rd.random())  

# رقم عشواي بين 1 و 10 (يقدر يكون فيه فاصلة)
print(rd.uniform(1, 10))  

# رقم عشواي صحيح بين 1 و 100
print(rd.randint(1, 100))  




# With 3 parameters
print(rd.randrange(1, 10, 2))  # Might print: 1, 3, 5, 7, or 9 (odd numbers only) (1+k*2)

# With 2 parameters
print(rd.randrange(5,10))     # Might print: 5, 6, 7, 8, or 9

# With 1 parameter
print(rd.randrange(5))         # Might print: 0, 1, 2, 3, or 4

mylist = ['7ajar', 'waraka','mi9as']
print(rd.choice(mylist))  # يمدلك قيمة من الليستة عشواي

clubs = ['madrid','barca','juve','ess']
rd.shuffle(clubs)  # يخلط القيم تاع الليستة
print(clubs)  


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# we want 3 different elements (no duplicates)
print(rd.sample(numbers, 3))  

# duplicates are allowed
print(rd.choices(numbers, k=3))  
