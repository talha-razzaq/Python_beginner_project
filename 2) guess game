# Guesing number game

import random 

def guess(x):
    random_number = random.randint(1, x)

    guess = 0

    while guess != random_number:
        guess = int(input(f"Enter the number between 1 to {x} : "))
        print("Our guess number is : ", guess)

        if guess < random_number:
            print("Sorry, guess again. Too low")

        elif guess > random_number:
            print("Sorry, guess again. Too high")

    print("Yap, congrats. You have guess the number which is : ", random_number)
guess(15)
