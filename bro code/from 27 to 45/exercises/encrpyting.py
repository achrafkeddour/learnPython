import random 
import string

chars = ' ' + string.ascii_letters + string.digits + string.punctuation
print(chars) #  abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

chars = list(chars)
# print(chars) # [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

key = chars.copy()
# print(key) # [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("\nNow this is my key\n")
random.shuffle(key) # koul mara resultat jdida ta3 tkhlat
print(key) # ['N', 'O', '-', 'S', 'Z', 'I', '6', ']', '1', 'A', 'z', 'R', '>', 'o', 'm', '3', '4', 'g', '.', 'L', 'u', 'X', '7', ';', 'H', '2', '=', 'e', '_', ',', '+', 'w', '!', '^', 'd', '$', 'T', '|', ' ', 'J', 'i', '5', '\\', 'c', '{', 'B', 'a', 's', 'E', 'h', 'F', 'j', 'p', 'f', '(', ':', '8', 'C', '`', '[', 'b', 'r', 'K', 'q', 'l', '<', '~', '/', 'G', '?', 'V', "'", '%', '}', 'k', 'Y', '&', 'v', 'P', '*', 'n', 'x', '"', '9', '#', 'Q', 'D', 't', '@', 'U', '0', 'W', 'M', ')', 'y'] 

print("-----------------------------------------------")
mytext = "helloword"
myencrypted_text = ''
for letter in mytext:
    index = chars.index(letter)
    # print(index)
    myencrypted_text += key[index]

print(myencrypted_text)

mydecrypted_text = ''

for letter in myencrypted_text:
    index = key.index(letter)
    mydecrypted_text += chars[index]
    
print(mydecrypted_text)
