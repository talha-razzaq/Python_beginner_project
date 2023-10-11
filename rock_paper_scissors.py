#Rock paper scissors game

import random

def play():
    user = input("What is your choice:[r / p / s] : ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won"

def is_win(player, opponent):
    # r > s, s > p, p > r

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):

        return True
    
print(play())
    