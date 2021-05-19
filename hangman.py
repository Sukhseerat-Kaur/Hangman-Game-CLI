import random
import string
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''
def print_image(IMAGES, num_of_wrong_guesses):
    print(IMAGES[num_of_wrong_guesses])

def is_input_valid(letter, letters_guessed):
    if(len(letter)==1 and (letter>='a' and letter<='z') and letter not in letters_guessed):
        return True
    return False

def hint(secret_word, letters_guessed):
    s=''
    for i in secret_word:
        if i not in letters_guessed:
            s+=i
    c = random.choice(s)
    letters_guessed.append(c)
    print("Ye le bhai hint pakad: {}".format(get_guessed_word(secret_word, letters_guessed)))
    print("")

def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    s = string.ascii_lowercase
    letters_left=''
    for i in s:
        if i not in letters_guessed:
            letters_left+=i
    return letters_left


def hangman(secret_word):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    remaining_lives=8
    print("Lives: {}".format(remaining_lives))

    num_of_wrong_guesses=-1
    is_hint_used=False
    letters_guessed = []

    while remaining_lives:
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))

        guess = input("Please guess a letter: ")
        letter = guess.lower()


        if letter=="hint" :
            if is_hint_used:
                print("Arre kitne hint chahiye bhai.. ek hi milta h.. aur ni milega")
                print("")
            else:
                is_hint_used=True
                hint(secret_word, letters_guessed)
            continue
        

        if not is_input_valid(letter, letters_guessed):
            print("Input a valid letter from available letters")
            print("")
            continue
        

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            print("")

            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            letters_guessed.append(letter)

            num_of_wrong_guesses+=1
            print_image(IMAGES, num_of_wrong_guesses)

            remaining_lives-=1
            print("Lives: {}".format(remaining_lives))
            if remaining_lives==0:
                print("LOL Loser.. The word was: {}".format(secret_word))
                print("You Died.. Game Over!!")
            print("")


secret_word = choose_word()
hangman(secret_word)
