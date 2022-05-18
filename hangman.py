import random, assets
from os import system, name

class Hangman():
    def __init__(self):
        # Banner Text
        self.banner = assets.banner
        # Menu Text
        self.menu = assets.menu
        # Dictionary of Categories
        self.categories = assets.categories
        # Dictionary of Scenes
        self.scenes = assets.scenes
        # Starting Scene
        self.scene = 0
        # Game Word
        self.word = ''
        # Game Board
        self.board = {}
        # Board Map
        self.board_map = {}
        # Guessed Letters
        self.guessed = []

    # Clearing the terminal
    def clear(self) -> None:
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    # Selecting a random word
    def select_word(self):
        '''Select a random word from a text file based on category selection'''
        self.clear()
        selection = 0
        # Validate user input for category selection
        while not selection:
            print(self.banner)
            try:
                selection = int(input(self.menu))
                # Set the word from the text files
                with open(self.categories[selection], "r") as wordlist:
                    self.word = random.choice(wordlist.readlines())
                    self.board = {index: letter for index, letter in enumerate(self.word)}
                    self.board_map = {index: not letter.isalpha() for index, letter in self.board.items()}
            # Handle invalid selections
            except KeyError:
                self.clear()
                print('Please enter a valid selection.')
                selection = 0
            # Handle strings
            except ValueError:
                self.clear()
                print('Please enter a number.')

    # Displaying a Game Board
    def display_board(self):
        '''Use map and board to display hidden letters'''
        hidden_letters = [self.board[i] if self.board_map[i] else '_' for i in self.board]
        print(*hidden_letters)

    # Updating the Board Map
    def update_map(self, guess: str):
        '''Update the map to track correct guesses'''
        for index, letter in self.board.items():
            if letter == guess:
                self.board_map[index] = True
    # Game Loop
    def play(self):
        '''Play the game!'''
        self.select_word()
        self.clear()
        while False in self.board_map.values() and self.scene < 6:
            # User Interface
            print(self.banner)
            print(self.scenes[self.scene])
            self.display_board()
            letter = input('Guess a letter: ').upper()
            # No penalty for guessing letters that have 
            if letter in self.guessed:
                self.clear()
                print('That letter has already been guessed!')
            # Correct guess, update game board
            elif letter in self.word:
                self.clear()
                self.guessed.append(letter)
                self.update_map(letter)
            # Wrong guess, update scene
            else:
                self.clear()
                self.guessed.append(letter)
                self.scene += 1
        # End Game
        print(self.banner)
        print(self.scenes[self.scene])
        print('GAME OVER!')


if __name__ == '__main__':
    game = Hangman()
    game.play()

