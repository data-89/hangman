import random
word_list = ['banana', 'watermelon', 'apricot', 'peach', 'plum']
word = random.choice(word_list)

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        if self.guess in self.word:
            print(f"Good guess! {self.guess} is in the word.")
        else:
            self.num_lives -= 1
            print(f"Sorry, {self.guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        while True:
            self.guess = input("Enter a single alphabetical character: ")
            if len(self.guess) == 1 and self.guess.isalpha():
                self.guess = self.guess.lower()
                self.check_guess()
                while self.num_lives != 0:
                    if self.guess in self.word:
                        for i in range(len(self.word)):
                            if self.word[i] == self.guess:
                                self.word_guessed[i] = self.guess
                                self.list_of_guesses.append(self.guess)
                                print(f"Good guess! '{self.guess}' is in the word.")
                    else self.guess in self.list_of_guesses:
                        print(f"You already tried that letter - '{self.guess}'. Try a different letter.")
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")      

my_hangman = Hangman()
Hangman.ask_for_input()