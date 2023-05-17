import random

class HangmanGame:
    def __init__(self):
        self.words = self.load_words_from_file("words.txt")
        self.chosen_word = random.choice(self.words)
        self.guessed_letters = []
        self.tries = 6

    def play(self):
        while self.tries > 0:
            self.display_status()

            if self.word_guessed():
                print("Congratulations! You guessed the word correctly.")
                return

            guess = self.get_valid_letter()

            if guess in self.guessed_letters:
                print("You have already guessed that letter. Try again.")
                continue

            self.guessed_letters.append(guess)

            if guess not in self.chosen_word:
                self.tries -= 1
                print("Wrong guess!")

            print()

        print("You ran out of tries. The word was:", self.chosen_word)

    def display_status(self):
        guessed_word = ""
        for letter in self.chosen_word:
            if letter in self.guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        print("Guessed word:", guessed_word)
        print("Tries left:", self.tries)
        print("Guessed letters:", self.guessed_letters)

    def word_guessed(self):
        return all(letter in self.guessed_letters for letter in self.chosen_word)

    @staticmethod
    def get_valid_letter():
        while True:
            guess = input("Enter a letter: ").lower()
            if len(guess) != 1:
                print("Please enter a single letter.")
            elif not guess.isalpha():
                print("Please enter a valid letter.")
            else:
                return guess

    @staticmethod
    def load_words_from_file(file_name):
        with open(file_name, "r") as file:
            return [line.strip() for line in file]

game = HangmanGame()
game.play()
