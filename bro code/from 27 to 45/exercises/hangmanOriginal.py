import random

# ✅ هاد الدالة تعرض شكل الراجل المشنوق حسب عدد المحاولات لي بقات

def display_man(attempts):
    hangman_stages = [
        """
           ----
           |  |
           |  O
           | /|\
           | / \\
           |
        """,
        """
           ----
           |  |
           |  O
           | /|\
           | /
           |
        """,
        """
           ----
           |  |
           |  O
           | /|\
           |
           |
        """,
        """
           ----
           |  |
           |  O
           | /|
           |
           |
        """,
        """
           ----
           |  |
           |  O
           |  |
           |
           |
        """,
        """
           ----
           |  |
           |  O
           |
           |
           |
        """,
        """
           ----
           |  |
           |
           |
           |
           |
        """
    ]
    print(hangman_stages[attempts])

# ✅ هاد الدالة تعطيك تلميحة على الكلمة (طولها فقط)
def display_hint(word):
    print(f"Hint: The word has {len(word)} letters.")

# ✅ كي يخسر اللاعب، نعرضولو الكلمة الصحيحة
def display_answer(word):
    print(f"The correct word was: {word}")

# ✅ الدالة الرئيسية وين راح نخدمو اللعبة
def main():
    words = ["python", "hangman", "developer", "keyboard", "program"]  # ✅ قائمة تاع الكلمات لي نختارو منها
    word = random.choice(words)  # ✅ نختارو كلمة عشوائية
    guessed_letters = []  # ✅ هنا نحتفظو بالحروف لي اللاعب جربها
    attempts = 6  # ✅ عدد المحاولات لي يقدر يغلط فيها
    
    display_hint(word)  # ✅ نعرضولو تلميحة على الكلمة
    
    while attempts > 0:
        display_man(attempts)  # ✅ نعرضولو حالة الراجل المشنوق حسب المحاولات لي بقاو
        
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print("Word: ", display_word)  # ✅ نعرضو الكلمة بلا الحروف لي مزال ماضربهاش
        
        guess = input("Guess a letter: ").lower()  # ✅ نطلبو منو يدخل حرف
        
        if guess in guessed_letters:
            print("You already guessed that letter.")  # ✅ اذا راه جرب نفس الحرف من قبل نقولولو
        elif guess in word:
            guessed_letters.append(guess)  # ✅ اذا الحرف موجود في الكلمة نزيدوه في لائحة الحروف لي راه ضربهم
            if all(letter in guessed_letters for letter in word):  # ✅ اذا اللاعب عرف كل الحروف، يربح
                print(f"Congratulations! You guessed the word: {word}")
                return # ✅ Stops the entire main() function, game ends!
        else:
            attempts -= 1  # ✅ اذا الحرف غلط، ننقصولو محاولة
            print("Incorrect guess!")
    
    display_man(attempts)  # ✅ نعرضولو الشكل النهائي تاع الراجل المشنوق
    print("Game over!")  # ✅ نعلموه بلي خسر
    display_answer(word)  # ✅ نعرضولو الكلمة الصحيحة

if __name__ == "__main__":
    main()  # ✅ تشغيل اللعبة
