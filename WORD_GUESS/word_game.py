"""
File: word_guess.py
-------------------
WORD GUESS GAME
CREATED BY:- KUSHAL KARAN
CREATED ON:- 29 MAY 2021
"""


import random


LEXICON_FILE = "Lexicon.txt"                                              # File to read word list from
# LEXICON_FILE = "TestLexicon.txt"                                        # File to read word list from
INITIAL_GUESSES = 8                                                       # Initial number of guesses player starts with
INITIAL_HINTS = 5                                                         # Initial number of hints player starts with
SPACES = "                                                          "     # 58 spaces
INTRO_SPACES = "                                              "           # 46 SPACES FOR INTRO MESSAGE


def play_game(secret_word):
    """
    INTRO-START
    """
    print(INTRO_SPACES+"============================================================================")
    print(INTRO_SPACES+"                  WELCOME TO THE TOUGHEST WORD GUESS GAME                   ")
    print(INTRO_SPACES+"                       You can only make 8 mistakes                         ")
    print(INTRO_SPACES+"                        Press '+' for taking HINTS                          ")
    print(INTRO_SPACES+"                              ALL THE BEST                                  ")
    print(INTRO_SPACES+"============================================================================")
    """
    INTRO-END
    """
    sec = secret_word             # sec is used when a correct letter is guessed then that letter is deleted from sec.
    guess = INITIAL_GUESSES       # maximum wrong guess allowed.
    blank = ""                    # for adding blank in place of word e.g book -> ----.
    length = len(secret_word)     # length of the secret word
    won = False                   # condition to check if user won or lost
    hint_count = INITIAL_HINTS    # Maximum hints allowed

    for i in range(length):       # this loop is for printing the initial blank word.
        blank = blank + "-"

    while guess != 0:
        ind = 0
        print(SPACES+"Your word looks like: " + blank)
        guessed = input(SPACES+"Enter your guess.You have " + str(guess) + " CHANCE and " + str(hint_count) + " HINTS left: ")
        guessed = guessed.upper()

        if len(guessed) == 1:
            for letter in secret_word:
                if guessed == letter:
                    if guessed in sec:
                        ind = sec.index(guessed)
                        blank = blank[:ind] + guessed + blank[ind+1:]
                        sec = sec[:ind] + "-" + sec[ind+1:]
                    else:
                        print(SPACES+"You already chose " + guessed)

            # Below code is to process hint
            if guessed == '+':
                if hint_count != 0:
                    hint_word = ""
                    for lt in sec:
                        if lt != '-':
                            hint_word = hint_word + lt
                    hint_len = len(hint_word)
                    ind = random.randint(0, hint_len - 1)
                    hint = hint_word[ind]
                    print(SPACES+"HINT: Try with: " + hint)
                    print("")
                    guess -= 1
                    hint_count -= 1
                else:
                    print(SPACES+"Sorry, No HINTS left")
                    print("")
            # Above code is to process hint

            # Below code is to check if guessed letter is correct or not
            if guessed not in secret_word:
                if guessed != '+':
                    print(SPACES+"OOPS!! There are no " + guessed + "\'s in the SECRET_WORD")
                    print("")
                    guess -= 1
            else:
                if guessed != '+':
                    print(SPACES+"That Guess is Correct!!!")
                    print("")
            # Above code is to check if guessed letter is correct or not

            if blank == secret_word:
                won = True
                break
            else:
                won = False

        else:
            print(SPACES+"Please Enter one letter.")
            print("")

    # Below code is to print winning or losing message:-
    if won:
        print(SPACES+"CONGRATS!!! YOU WON. ")
        print(SPACES+"You took " + str(8-guess) + " CHANCES and " + str(5-hint_count) + " HINTS to guess the word: " + secret_word)
        print("")
    else:
        print(SPACES+"GAME OVER")
        print(SPACES+"OOPS!!! YOU LOST. THE WORD WAS: " + secret_word)
        print("")
    # Above code is to print winning or losing message


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    word = []
    with open(LEXICON_FILE) as f:
        for words in f:
            words = words.strip()
            word.append(words)
    length = len(word) - 1
    rand = random.randint(0, length-1)
    return word[rand]


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    turn = 'Y'
    while True:
        if turn == 'Y':
            secret_word = get_word()
            play_game(secret_word)
            turn = input(SPACES+"Do you want to play again? (Y/N): ")
            turn = turn.upper()
        elif turn == 'N':
            break
        else:
            print("")
            print(SPACES+"Please Enter Y or N")
            turn = input(SPACES+"Do you want to play again? (Y/N): ")
            turn = turn.upper()
    print("")
    print(SPACES+"HAVE A GOOD DAY!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()