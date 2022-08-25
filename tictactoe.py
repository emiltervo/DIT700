bräda = {'1': ' ', '2': ' ', '3': ' ', '4': ' ',
         '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}


def hasThreeInRow(tecken):
    return ((bräda['1'] == tecken and bräda['2'] == tecken and bräda['3'] == tecken) or
            (bräda['4'] == tecken and bräda['5'] == tecken and bräda['6'] == tecken) or
            (bräda['7'] == tecken and bräda['8'] == tecken and bräda['9'] == tecken) or
            (bräda['1'] == tecken and bräda['4'] == tecken and bräda['7'] == tecken) or
            (bräda['2'] == tecken and bräda['5'] == tecken and bräda['8'] == tecken) or
            (bräda['3'] == tecken and bräda['6'] == tecken and bräda['9'] == tecken) or
            (bräda['1'] == tecken and bräda['5'] == tecken and bräda['9'] == tecken) or
            (bräda['3'] == tecken and bräda['5'] == tecken and bräda['7'] == tecken))


def fullbräda():
    for key in bräda:
        if bräda[key] == ' ':
            return False
    return True


def print_board():
    print(bräda['1'] + '|' + bräda['2'] + '|' + bräda['3'])
    print('-+-+-')
    print(bräda['4'] + '|' + bräda['5'] + '|' + bräda['6'])
    print('-+-+-')
    print(bräda['7'] + '|' + bräda['8'] + '|' + bräda['9'])


def placeSign(tecken, position):
    bräda[position] = tecken


def play():
    gameover = False
    print('Welcome to Tic Tac Toe!')
    print_board()
    while True:
        player1_tecken = input('Player 1, choose X or O: ').upper()
        while player1_tecken not in ['X', 'O']:
            player1_tecken = input('Player 1, choose X or O: ').upper()
        player2_tecken = 'O' if player1_tecken == 'X' else 'X'
        print('Player 1 is ' + player1_tecken +
              ' and Player 2 is ' + player2_tecken)
        player1_turn = True
        while not gameover:
            if player1_turn:
                position = input('Player 1, choose a position: ')
                while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    position = input('Player 1, choose a position: ')
                placeSign(player1_tecken, position)
                print_board()
                player1_turn = False
            else:
                position = input('Player 2, choose a position: ')
                while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    position = input('Player 2, choose a position: ')
                placeSign(player2_tecken, position)
                print_board()
                player1_turn = True
            if hasThreeInRow(player1_tecken):
                print('Player 1 has ThreeInRows!')
                gameover = True
                break
            elif hasThreeInRow(player2_tecken):
                print('Player 2 has ThreeInRows!')
                gameover = True
                break
            elif fullbräda():
                print('Draw!')
                gameover = True
                break
        if not input('Play again? (y/n) ').lower().startswith('y'):
            break


play()
