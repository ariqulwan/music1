#!/usr/bin/env python

import random

def main():
    """start a pop singer guessing game."""
    print("guess the pop singer")
    
    pop_singer = ["zayn","lorde","shakira","halsey","corook"]
    
    name = input("masukkan nama anda:")
    print("welcom",(name))

    x = random.choice(pop_singer)
    guess = None

    tries=0
    
    for tries in range (3):

        guess = str(input("\n what a music thingking of?"))

        if x == guess:
            print("you guessed {}. congratulations you got it right".format(guess))
            break
        else :
            print("you guessed {}.Unfortunately you got a wrong answer.please try again!".format(guess))
    else :
        print("you've guessed 3 times.the correct answer is :" , x )
main()