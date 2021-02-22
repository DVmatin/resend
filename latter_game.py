import random
import os
import sys

#make list of words
words = [
    'apple',
    'bennana',
    'coconut',
    'straw berry',
    'lime',
    'kumquat',
    'lemon',
    'grapefruit',
    'kumquat',
    'blueberry',
    'melon',
]

# os.system('cls' if os.name ='nt')
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')   


def draw(bad_guesses, good_guesses, secret_word):
    clear()
    print('strikes : {}/7'.format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter, end = ' ')
        print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end = ' ')
        else:
            print('_', end = ' ')   


def get_guess(bad_guesses, good_guesses):
    while True:
        print(' ')
        guess = input("guess a letter:").lower()
        #take guess
        if len(guess) != 1:
            print("YOU CAN ONLU GUESS A SINGEL LETTER:")
            continue
        #draw guess latter and striks
        elif guess in bad_guesses or guess in good_guesses:
            print("you have alredy guess that letter!")
            continue
        elif not guess.isalpha():
            print("you can only guess letters!")
        else:
            return guess   


def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guess= []
    good_guess = []

    while True:
        draw(bad_guess, good_guess, secret_word)
        guess = get_guess(bad_guess, good_guess)

        if guess in secret_word:
            good_guess.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guess:
                    found = False
            if found:
                print ('you win')
                print (" The secret word was {}".format(secret_word))
                done = True
        else:
            bad_guess.append(guess)
            if len(bad_guess) == 7:
                draw (bad_guess, good_guess, secret_word)

                print ("YOU Cant Found It")
                print("the secret word was {}".format(secret_word))
                done = True
        if done:
            play_again = input("Would you like Play again? [y/n]").lower()

            if play_again != 'n':
                return play(done = False)
            else:
                sys.exit()    

def welcome():
    start = input("press enter/return to start or Q to quit").lower()
    print ('Wlcome to Letter game!')
    if start ==  'q':
        print("Bye,Bye!")
        sys.exit()
    else:
        return True


done = True
while True:
    clear()
    welcome()
    play(done)