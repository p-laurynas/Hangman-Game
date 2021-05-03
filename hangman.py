import random


class HangmanGame:

    def __init__(self):
        self.words = ['python', 'java', 'kotlin', 'javascript']
        self.word = None
        self.result = None
        self.attempts = 8
        self.guesses = set()

    def main(self):
        print(*"HANGMAN")
        while True:
            user_option = input('Type "play" to play the game, "exit" to quit: ')
            if user_option == 'play':
                self.play_game()
            elif user_option == 'exit':
                break

    def play_game(self):
        self.word = random.choice(self.words)
        self.result = '-' * len(self.word)
        while self.result != self.word and self.attempts > 0:
            print(f"\n{self.result}")
            guess = input("Input a letter: ")
            self.take_guess(guess) if self.check_guess(guess) is True else print(self.check_guess(guess))
        print(self.check_result())

    def take_guess(self, guess):
        self.guesses.add(guess)
        if guess not in self.word:
            print("That letter doesn't appear in the word")
            self.attempts -= 1
        else:
            indices = [index for index, letter in enumerate(self.word) if guess == letter]
            self.result = list(self.result)
            for index in indices:
                self.result[index] = guess
            self.result = ''.join(self.result)

    def check_guess(self, guess):
        if guess in self.guesses:
            return "You've already guessed this letter"
        elif len(guess) != 1:
            return "You should input a single letter"
        elif not guess.islower():
            return "Please enter a lowercase English letter"
        else:
            return True

    def check_result(self):
        return f"You guessed the word {self.word}!\nYou survived!" if self.result == self.word else "You lost!"


if __name__ == '__main__':
    HangmanGame().main()
