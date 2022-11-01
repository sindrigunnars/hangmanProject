import singleGame as hang
import leaderboard as ldrbrd

class HangmanGame:
    def __init__(self):
        self.score = 0
        self.highscore = 0
        self.username = None

    def __guess_setting(self):
        self.guess_number = int(input('How many guesses in this game?\nRecommended levels:\n\tEasy = 10\n\tNormal = 5\n\tHard = 2\nValue: '))

    def __initialize_words(self):
        with open('wordlist.txt') as file:
            self.word_database = list(file)

    def __continue(self):
        print(f'Your score is currently {self.score}, high score this round is {self.highscore}')
        do_continue = input('Press Q to quit game, press any other key to continue\n').lower()
        if do_continue == 'q':
            print('You exited the game')
            return False
        return True

    def __add_words(self):        
        word = (input("Add Word "))
        with open("wordlist.txt", "a") as wordlist:
            wordlist.write("\n" + word)
        print("Word added!")

    def __change_username(self):
        self.username = input('Input username, Username: ')
        print("Username changed!")
    
    def __display_leaderboard(self):
        while True:
            with open('leaderboard.csv') as ldr:
                self.ldr_length = int(input('How many scores do you want to see?\n'))
                display = ldrbrd.Leaderboard(ldr, self.username, self.ldr_length)
                print(display)
            exit_cond = input('Press Q to quit to main menu!').lower()
            if exit_cond == 'q':
                break

    def __save_session(self):
        with open('leaderboard.csv', 'a') as leaderboard:
            leaderboard.write(f'\n{self.username};{self.score}')

    def __play(self):
        self.__initialize_words()
        self.__guess_setting()
        while True:
            hangman = hang.Hangman(self.word_database, self.guess_number)
            hangman.game_round()
            self.score += int(hangman.result * (10/hangman.guess_limit))
            if hangman.result == 1 and self.highscore < self.score:
                self.highscore = self.score
            if hangman.result == 0:
                self.score = 0
            if not self.__continue():
                save_bol = input(f"Press S to save your score ({self.highscore}) or press any other key to go to main menu\n").lower()
                if save_bol == "s":
                    self.__save_session()
                    print("Scores saved")
                break

    def main_menu(self):
        while True:
            if self.username == None:
                self.username = input('Input username before you start, Username: ')
            main_input = input(f'Welcome to hangman {self.username}!\nWhat do you want to do? Press\n1: Play Hangman\n2: Display Leaderboard\n3: Add word\n4: Change Username\nQ: Exit menu\n').lower()
            if main_input == '1':
                self.__play()
            elif main_input == '2':
                self.__display_leaderboard()
            elif main_input == "3":
                self.__add_words()
            elif main_input == "4":
                self.__change_username()
            elif main_input == 'q':
                print('You exited the game')
                break
            
if __name__ == '__main__':
    game = HangmanGame()
    game.main_menu()