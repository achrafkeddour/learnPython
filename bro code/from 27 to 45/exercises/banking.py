balance = 0

def deposit(amount):
    global balance
    balance += amount
    print(f"Changes Done , Now you have {show_balance()} dinars")

def arfad(amount):
    global balance
    
    if balance > 0:
        if amount < balance:
            balance -= amount
            print(f"Changes Done , Now you have {show_balance()} dinars")
        elif amount > balance:
            print(f"you have only {balance} sorry !")
            
    if balance == 0 or balance < 0 :
        print(f"your balance is {balance}, you must deposit something !")

def show_balance():
    global balance
    return balance



def main():
    print("Welcome to our banking program ! ")
    while True:
        choice = input("\nenter \n 1. for deposit an amount \n 2. bach tarfad chwiya drahem \n 3. bach tchouf ch7al 3ndk\n")
    
        if choice == '1':
            amount = int(input("enter an amount : "))
            deposit(amount)
           
        elif choice == '2':
            amount = int(input("enter an amount : "))
            arfad(amount)
            
        elif choice == '3':
            print(f"you have {show_balance()} dinars")
        elif choice in ['q','exit','quit','stop'] :
            break

if __name__ == '__main__':
    main()