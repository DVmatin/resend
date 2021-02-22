import random

number = random.randint(1, 10)

def run_game():
    guesses = []
    gauss = 0

    while len (guesses) <= 5:
        try:
            guess = int(input("enter your guess in rang 1 to 10: "))
        except ValueError:
            print("{} isnt a number!".format(guess))  
        else:
            if guess == number:
                print (" bang bang you got it number is {}. ".format(number))
                break
            elif guess < number:
                print("number is higher than {}".format(guess))
            elif guess > number:
                print("number is lesser than {}".format(guess))
            else:
                print("isnt true your guess")   
        guesses.append(guess)
    else:
        print("you cant find the number! the number is{}".format(number))


    play_again = input("do you wana play again? [Y/N]")

    if play_again != 'N':
        run_game()
    else:
        print("bye bye.see you later soon")
run_game()