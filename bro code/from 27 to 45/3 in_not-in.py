""" in , not in"""

email = "achrafgmail.py"

if '@' not in email or '.' not in email:
    print("please enter a real email, example@mail.com")
    print("your email should contain @ and .")
else :
    print('correct')
    
dict = {
    "name":"john",
    "fname":"smith",
    "age":50,
    "coutry":"usa"
}

if input("think of a key ") in dict: 
    print("it exists") # if name , fname , age , country
else:
    print("doesn't exist") 
    
    
def signup():
    while True:
        facebook_name = input("enter your facebook name : ")
        facebook_password = input("enter your password : ")
        if facebook_name in facebook_password:
            print("your facebook name shouldn't be in the password ")
            print("password refused")
        else:
            print("password accepted ")
            break
signup()

print("fin de sign up et passer à autre chose")

