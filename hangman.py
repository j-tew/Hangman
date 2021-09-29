import random
from os import system, name


'''------------------------------------------------------------
Welcome to my Hangman game!

**EXTRAS** (Future Updates)
- [ ] Beginning UI
        - Categories (make sports a submenu?)
------------------------------------------------------------'''


# Banner
banner = '''
 _   _
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
|  _  | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/
'''

# Dictionary for the scenes
scene = {
    0: '''
         ___________ 
        |           |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |''',

    1: '''
         ___________ 
        |           |
        |          ,,,
        |         (X_X)
        |
        |
        |
        |
        |
        |
        |
        |
        |''',

    2: '''
         ___________ 
        |           |
        |          ,,,
        |         (X_X)
        |           |
        |           |
        |
        |
        |
        |
        |
        |
        |''',

    3: '''
         ___________ 
        |           |
        |          ,,,
        |         (X_X)
        |         \_|
        |           |
        |
        |
        |
        |
        |
        |
        |''',

    4: '''
         ___________ 
        |           |
        |          ,,,
        |         (X_X)
        |         \_|_/
        |           |
        |
        |
        |
        |
        |
        |
        |''',

    5: '''
         ___________ 
        |           |
        |          ,,,
        |         (X_X)
        |         \_|_/
        |           |
        |          /
        |         /
        |
        |
        |
        |
        |''',

    6: '''
         ___________ 
        |           |
        |          ,,,
        |         (X_X)
        |         \_|_/
        |           |
        |          / \\
        |         /   \\
        |
        |
        |
        |
        |'''
}

menu = '''
1) Baseball Teams
2) Country Artists
3) Disney Movies

'''

# Dictionary of categories
categories = {
    1: "baseball_teams.txt",
    2: "country_artists.txt",
    3: "disney.txt"
}

# Credit to ChickenParm for a function to make the game not junk up the terminal
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Selecting a random word.
def wordGen(sel, catDict):
    wordlist = open(catDict[sel], "r")
    words = wordlist.readlines()
    word = random.choice(words)
    wordlist.close()
    return word
# testWord = "devildog"

# Updating the game board with guesses
def updateBoard(brd, wrd, ltr):
    places = []
    index = 0
    for i in wrd:
        if i == ltr:
            places.append(index)
        index += 1
    for i in places:
        brd[i] = ltr
    return brd

def updateWord(wrd, ltr):
    trans = wrd.maketrans(ltr, "-", "\n")
    wrd = wrd.translate(trans)
    return wrd

# Accepting guesses
def getGuess():
    guess = input("Please Enter A Letter: ")
    return guess.upper()

# Generating a board of underscores to display
def boardGen(wrd):
    letters = list(wrd)
    letters.remove(letters[-1])
    board = []
    for i in letters:
        if i.isalpha():
            board.append("_")
        elif i == " ":
            board.append(" ")
    return board

# Generate the Phrase

clear()
print(banner)
selection = input(f"Please Select a Category:\n{menu}")        
word = wordGen(int(selection), categories)
board = boardGen(word)

# Make it Loop
key = 0

### TESTING ###
# print(word)
# print(*board)
# letter = getGuess()
# update(board, word, letter)
# print(word)
# print(*board)

# Game Loop
while word.count("-") < len(word):
    # Keeping the game board clean
    clear()
    print(banner)
    # Hangman scenes
    print(scene[key])
    # Word to be guessed
    print(f"Secret Word: ", *board, "\n")
    # If dude is complete or if the word is complete break the loop
    if key == 6 or "_" not in board:
        break
    # Take guesses as input
    letter = getGuess()
    # Checking guesses and updating the scene and board accordingly
    if len(letter) > 1 or len(letter) < 1:
        key += 1
    elif letter == " ":
        key += 1
    elif letter in word:
        board = updateBoard(board, word, letter)
        word = updateWord(word, letter)
    else:
        key += 1
# Ending the Game
if "_" not in board:
    clear()
    print(banner)
    print(scene[key])
    print(f"Secret Word: ", *board)
    print("\tYOU WIN!!!")
else:
    clear()
    print(banner)
    print(scene[6], "GAME OVER!!!")
