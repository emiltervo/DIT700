from array import *

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]]


def isWinner(board, spelare1, spelare2):
    # This function checks if any winner is winning
    winner = False
    # Check the rows
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == spelare1):
            winner = True
            print("Player " + spelare1 + ", you won!")

        elif (board[row][0] == board[row][1] == board[row][2] == spelare2):
            winner = True
            print("Player " + spelare2 + ", you won!")

    # Check the columns
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == spelare1):
            winner = True
            print("Player " + spelare1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == spelare2):
            winner = True
            print("Player " + spelare2 + ", you won!")

    # Check the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == spelare1:
        winner = True
        print("Player " + spelare1 + ", you won!")

    elif board[0][0] == board[1][1] == board[2][2] == spelare2:
        winner = True
        print("Player " + spelare2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == spelare1:
        winner = True
        print("Player " + spelare1 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == spelare2:
        winner = True
        print("Player " + spelare2 + ", you won!")

    return winner


def printboard(board):
    for r in board:
        for c in r:
            print(c, end=" ")
        print()


def player_turns(count, spelare1, spelare2):
    if count % 2 == 0:
        count += 1
        return spelare1

    else:
        return spelare2


def placeSign(x, y, spelare):
    tecken = spelare
    board[y - 1][x - 1] = tecken


def play():
    vinnare = False
    count = 0
    printboard(board)
    spelare1 = input("What sign do you want Player one? X or O?" + "\n")
    spelare2 = 'O' or "o" if spelare1 == 'X' or "x" else 'X'
    print("\n" + str(spelare1) + " vs " +
          str(spelare2) + "\n" + "Let's Play!")
    while vinnare == False:
        printboard(board)
        spelare = player_turns(count, spelare1, spelare2)
        positionx = int(input(f"{spelare} Välj en position: x 1-3:" + "\n"))
        positiony = int(input(f"{spelare} Välj en position: y 1-3:" + "\n"))
        if board[positiony - 1][positionx - 1] != "-":
            continue
        placeSign(positionx, positiony, spelare)
        if isWinner(board, spelare1, spelare2):
            break
        count += 1


play()
