"""list comprehension""" 

#instead of using this 
double = []
for i in range(1,11):
    double.append(i*2)
print(double)
#we can use this 
triple = [ i*3 for i in range(1,11)]
print(triple)

""" la formule génarale : newlist = [f(x) for x in oldlist]"""


fruits = ['abricot', 'banana','orange','strawberry']
upperfruits = [fruit.upper() for fruit in fruits] #['ABRICOT', 'BANANA', 'ORANGE', 'STRAWBERRY']

first_chars = [fruit[0] for fruit in fruits]
print(first_chars)

nums =[1, 2, -4, 5, -6, -10,-7,0]

positive_nums = [num for num in nums if num > 0]
print(f"positive nums : {positive_nums}")

odd_nums = [num for num in nums if not num % 2 == 0 ]
print(f"odd nums {odd_nums}")