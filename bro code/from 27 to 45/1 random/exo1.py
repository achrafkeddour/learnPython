import random as rd

mynum = rd.randint(1,100)

user_num = -1
essays = 0 
while not mynum == user_num:
    user_num = input("guess the integer (from 1 to 100) that the computer choosen : ")
    if not user_num.isdigit():
        print("we want an integer not letters")
    else:
        user_num = int(user_num)
        if user_num == mynum:
            print(f"correct, you got it after {essays} times")
            
        elif user_num > mynum:
            print("it's smaller than this !")
            essays+=1
            
        elif user_num < mynum:
            print("it's bigger than this !")
            essays+=1