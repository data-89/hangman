import random
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
            print(f"Sorry, {self.guess} is not in the word. Try again.")

    def ask_for_input(self):
        while self.num_lives != 0:
            guess = input("Enter a single alphabetical character: ")
            if len(guess) == 1 and guess.isalpha():
                self.guess = guess.lower()
                self.check_guess(guess)
                if self.guess in self.word:
                    for i in range(len(self.word)):
                        if self.word[i] == self.guess:
                            self.word_guessed[i] = self.guess
                            self.list_of_guesses.append(self.guess)
                elif self.guess in self.list_of_guesses:
                     print(f"You already tried that letter - '{self.guess}'. Try a different letter.")
                else:
                    self.num_lives -= 1
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")   
        if self.num_lives == 0:
            print("Game over. The word was:", self.word)

word_list = ['banana', 'watermelon', 'apricot', 'peach', 'plum']
my_hangman = Hangman(word_list)
print(my_hangman.ask_for_input())