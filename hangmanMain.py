import random as rnd
import os

class Hangman:
    def __init__(self, words, guess_limit = 6):
        self.guess_limit = guess_limit
        self.words = words
    
    def get_word(self):
        self.word = list(rnd.choice(self.words).lower().strip())
        self.display_word = ['-'] * len(self.word)

    def _check_guess(self, string):
        guess_bool = False
        if len(string) == 1:
            for i, j in enumerate(self.word):
                if j == string:
                    self.display_word[i] = j
                    guess_bool = True
        if string == ''.join(self.word):
            self.display_word = list(string)
            guess_bool = True
        if guess_bool:
            print(f'The word contains {string}')
        else:
            print(f'The word does not contain {string}')
        return guess_bool

    def _game_over(self):
        game_over = False
        if self.word == self.display_word:
            print(f'You won! The word was {"".join(self.word)}')
            game_over = True
            self.result = 1
        elif self.guess_limit == self.guesses:
            print(f'You lost! The word was {"".join(self.word)}')
            game_over = True
            self.result = 0
        return game_over

    def game_round(self):
        self.get_word()
        self.guesses = 0
        while True:
            print(f'{"".join(self.display_word)}\tGuesses left = {self.guess_limit - self.guesses}')
            input_char = str(input('What is your guess?'))
            if not self._check_guess(input_char):
                self.guesses += 1
            if self._game_over(): break
            os.system('clear')

if __name__ == '__main__':
    game = Hangman()
    game.play()



