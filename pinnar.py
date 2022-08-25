from random import randrange
antal = (randrange(15, 25))

spelare1 = input("What is your name Player One?" + "\n")
spelare2 = input("What is your name Player Two?" + "\n")
print("\n" + str(spelare1) + " vs " + str(spelare2) + "\n" + "Let's Play!")


def player_turns(total_turns):
    if total_turns % 2 == 0:
        return spelare1
    else:
        return spelare2


total_turns = 0
while antal > 0:
    player = player_turns(total_turns)
    val = int(input(f"{player} Välj en eller 2 pinnar: "))
    antal = antal - val
    if antal <= 0:
        print(f"{player_turns(total_turns)} vinner!")
        break
    total_turns += 1
