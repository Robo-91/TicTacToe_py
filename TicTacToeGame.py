welcome_message = f'Welcome to Tic-Tac-Toe!'
game_ending_message = f'Thanks for playing!'
players = ['X','O']
boardmarks = { 
    1: ' ',
    2: ' ',
    3: ' ',
    4: ' ',
    5: ' ',
    6: ' ',
    7: ' ',
    8: ' ',
    9: ' '
 }
board_keys = [k for k in boardmarks]

board = []

def display_board():
    for key in boardmarks:
        if key in [3,6,9]:
            board.append(f'{boardmarks[key]}\n-+-+-\n')
        else:
            board.append(f'{boardmarks[key]}|')
    return board

print(''.join(display_board()))
##print(boardmarks)
##print(welcome_message)
##print(board_keys)