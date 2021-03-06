#!/usr/bin/env python3

# rps.py
# Plays a game of rock, paper, scissors

import sys
import random

userScore = 0
enemScore = 0
allowed = ('r', 'p', 's')

def main():
    random.seed()

    print("ROCK, PAPER, SCISSORS")

    while True:
        hand = getHand()
        enem = random.choice(allowed)

        if hand == 'q':
            break
        
        winner = calculate(hand, enem)
        print("You: {}  Comp: {}".format(userScore, enemScore), end="\n\n")

    sys.exit(0)


def getHand():
    global allowed

    while True:
        hand = input("Enter your move: (r)ock (p)aper (s)cissors (q)uit: ").strip().lower()

        if hand in allowed or 'q':
            return hand
        
        else:
            print()


def calculate(hand, enem):
    global userScore
    global enemScore

    values = {'r':'rock', 'p':'paper', 's':'scissors'}

    print("{} vs {}".format(values[hand], values[enem]))

    if hand == enem:
        print("Its a tie!")

    elif (hand == 'r' and enem == 's') or (hand == 'p' and enem == 'r') or (hand == 's' and enem == 'p'):
        userScore += 1
        print("You win!")

    else:
        enemScore += 1
        print("You lose!")


if __name__ == "__main__":
    main()
