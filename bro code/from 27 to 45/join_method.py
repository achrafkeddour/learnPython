"""the .join() method is used to combine elements of an iterable (like: list, tuple) into only one string 
It places the specified separator between each element """

# separator.join(iterable)


# ex1
words = ["hello","world","python","is","easy"]
sentence = " - ".join(words)
print(sentence) # hello - world - python - is - easy

# ex2 
data = ["Alice", "25", "Engineer"]
csv_line = ",".join(data)
print(csv_line)  # Output: "Alice,25,Engineer"


# ex3 : creating a path
folders = ["Users","Achraf","Documents","python","app.py"] 
path = "/".join(folders)
print(path) # Users/Achraf/Documents/python/app.py


# ex4 : using a tuple 
mytuple = ("h","e","l","l","o")
myword = "".join(mytuple)
print(myword) # hello


# ex5 : using input
user_input = input("Enter letters without spaces: ")  # Example input: abcd
formatted = " ".join(user_input)
print(formatted) # a b c d


# simple encoding 
mypasscode = "code123"
encoded = "*".join(mypasscode)
print(encoded) # c*o*d*e*1*2*3

decoded = encoded.replace("*","")
print(decoded) # code123




"""❌ Joining non-string elements will cause an error"""
# numbers = [1, 2, 3, 4, 5]  # Integers, not strings
# print(",".join(numbers))  # TypeError: sequence item 0: expected str instance, int found

"""✅ Solution: Convert to Strings First"""
numbers = [1, 2, 3, 4, 5]
print(','.join(map(str,numbers))) # 1,2,3,4,5


""" map(function, iterable) applies a function to each element of the iterable (str is a function that convert integers to strings)"""
def myfunction(x):
    return x.upper()  

names = ['ahmed','mohamed','aissa']
upper_numbers = ' - '.join(map(myfunction, names))  
print(upper_numbers)  # AHMED - MOHAMED - AISSA

