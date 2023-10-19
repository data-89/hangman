import random
word_list = ['banana', 'watermelon', 'apricot', 'peach', 'plum']
word = random.choice(word_list)

def check_guess(word, guess):
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Enter a single alphabetical character: ")
        if len(guess) == 1 and guess.isalpha():
            guess = guess.lower()
            check_guess(word, guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")      

ask_for_input()


