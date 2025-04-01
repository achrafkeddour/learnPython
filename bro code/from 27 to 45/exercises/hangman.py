import random

def display_man(numOfTry):
    hangman_stages = ["""
                     |  O
                     | / \\
                      """,
                      """
                     |  O
                     | / 
                      """,
                      """
                     | O
                     | 
                      """,
                      """ 
                     | 
                     | 
                      """
                      ]
    print(hangman_stages[numOfTry])
    # here i put a list for the man size and a print() to print the man
    
def display_hint(word):
    print(f"the length of the word is {len(word)}") #talmi7 about the word 

def display_answer(word):
    print(f"sadly , you're wrong , the word is : {word}")    
    
def main():
    listOfWords = ['python','numpy','pandas','matplotlib']
    word = random.choice(listOfWords)
    guessed_letters = []
    display_hint(word)
    essays = 3
    
    while essays > 0:
        display_man(essays)
        displayed_word = ' '.join([letter if letter in guessed_letters else "--" for letter in word])
        print(f"the word is {displayed_word}")

        guess = input("guess a letter please : ").lower()
        
        if guess in guessed_letters:
            print("you found it before ! guess another ")
            
        elif guess in word:
            guessed_letters.append(guess)
            if all(x in guessed_letters for x in word): # if they are the same 
                print(f"congratulations ! you got it , and the word is {word}")
                return
        
        else:
            essays -= 1
            print(f"incorrect answer, il vous reste {essays} essays ")
            
    print(f"the num of essays is {essays} so game over ! ")
    display_man(essays)
    display_answer(word)
        

if __name__ == '__main__':
    main()
