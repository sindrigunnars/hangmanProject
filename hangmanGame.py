import hangmanMain as hang
import leaderboard as ldrbrd
import os

class HangmanGame:
    def __init__(self):
        self.score = 0
        self.highscore = 0
        self.username = None
        self.empty_user = True
        self.ldr_length = 5

    def _guess_setting(self):
        self.guess_number = int(input('How many guesses in this game?\nRecommended levels:\n\tEasy = 10\n\tNormal = 5\n\tHard = 2\n'))

    def initialize_words(self):
        with open('wordlist.txt') as file:
            self.word_database = list(file)

    def _continue(self):
        print(f'Your score is currently {self.score}')
        do_continue = str(input('Press Q to quit to main menu and save score, press any other key to continue')).lower()
        if do_continue == 'q':
            print('You exited the game')
            return False
        return True

    def main_menu(self):
        while True:
            if self.empty_user:
                self.username = str(input('Input username before you start, Username: '))
                self.empty_user = False
            main_input = str(input('Welcome to hangman!\nWhat do you want to do? Press\n1: Play Hangman\n2: Display Leaderboard\nQ: Exit game'))
            if main_input == '1':
                self.play()
            if main_input == '2':
                self.display_leaderboard()
            if main_input == 'q':
                break

    def display_leaderboard(self):
        while True:
            with open('leaderboard.csv') as ldr:
                self.ldr_length = int(input('How many scores do you want to see?'))
                display = ldrbrd.Leaderboard(ldr, self.ldr_length)
                print(display)
            exit_cond = input('Press Q to quit to main menu!').lower()
            if exit_cond == 'q':
                break

    def _save_session(self):
        with open('leaderboard.csv', 'a') as leaderboard:
            leaderboard.write(f'\n{self.username};{self.score}')

    def play(self):
        self.initialize_words()
        self._guess_setting()
        while True:
            hangman = hang.Hangman(self.word_database, self.guess_number)
            hangman.game_round()
            self.score += int(hangman.result * (10/hangman.guess_limit))
            if hangman.result == 1 and self.highscore < self.score:
                self.highscore = self.score
            if not self._continue(): 
                self._save_session()
                break

if __name__ == '__main__':
    game = HangmanGame()
    game.main_menu()