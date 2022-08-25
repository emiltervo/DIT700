import random

försök = []


def show_score():

    if len(försök) <= 0:
        print("There is no high score")
    else:
        print("The highest score is {}".format(min(försök)))
