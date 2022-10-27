import hangmanMain as hang

class HangmanGame:
    def __init__(self):
        self.score = 0
        self.highscore = 0

    def _guess_setting(self):
        self.guess_number = int(input('How many guesses in this game?\nRecommended levels:\n\tEasy = 10\n\tNormal = 5\n\tHard = 2\n'))

    def initialize_words(self):
        # with open('words.txt') as file:
        #     self.word_database = list(file)
        self.word_database = ['literal']

    def _continue(self):
        print(f'Your score is currently {self.score}')
        do_continue = str(input('Press q/Q to quit game, press any other key to continue')).lower()
        if do_continue == 'q':
            print('You exited the game')
            return False
        return True

    def _save_session(self):
        username = str(input('Username: '))
        with open('leaderboard.csv', 'a') as leaderboard:
            leaderboard.write(f'\n{username};{self.score}')

    def play(self):
        self.initialize_words()
        self._guess_setting()
        while True:
            hangman = hang.Hangman(self.word_database, self.guess_number)
            hangman.game_round()
            self.score += int((hangman.result * (10/hangman.guess_limit)))
            if hangman.result == 1 and self.highscore < self.score:
                self.highscore = self.score
            if not self._continue(): 
                self._save_session()
                break

if __name__ == '__main__':
    game = HangmanGame()
    game.play()