import string
""" What is import string?
The string module in Python provides a collection of constants and
utility functions that make it easier to work with text data."""


print(string.ascii_letters)  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_lowercase)  # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase)  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)  # '0123456789'
print(string.hexdigits)  # '0123456789abcdefABCDEF'
print(string.octdigits)  # '01234567'
print(string.punctuation)  # '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.whitespace)  # ' \t\n\r\x0b\x0c' (space, tab, newline, etc.)

print("------------------------------------------------------------------\n")
print(string.printable)  # Combination of digits, letters, punctuation, and whitespace + Some additional control chars like \x0b and \x0c 




mychars = string.punctuation + string.ascii_letters + string.digits + string.whitespace

print(mychars) # result 1 
print(string.printable) # result 2 (fiha 3fays sghar zyada 3la result 1 )
