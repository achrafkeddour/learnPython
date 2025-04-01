import random

money = 100

def spin():
    symbols = ['🍒', '🔔', '⭐', '🍊', '🍉']
    return [random.choice(symbols) for _ in range(3)]

def check_win(list,bet):
    global money
    print(list)
    if list[0] == list[1] == list[2]:
        money += bet
        print("ga3 jaw kifkif !")
        print(f"haka nzidoulk {bet} 3la drahmek , wyweli 3ndk {money} dinars")
    elif (list[0] == list[1] or list[0] == list[2] or list[1] == list[2]) :
        money +=2
        print(f"you have +2 now , your money become {money}")
    else:
        print(f"you lost this round. Now you have {money} dinars")
def main():
    global money
    print(f"hello , you have {money} dinars")
    
    while money > 0:
        bet = int(input("bch7al rak hab t9amer : "))
        money -= bet
        result = spin()
        check_win(result,bet)

main()        
