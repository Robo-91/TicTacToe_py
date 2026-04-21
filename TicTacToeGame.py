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

## Update Board with the selection that the current player has made
current_player = 'X'
player_move = int(input(f"What is {current_player}'s move? (1-9))"))
boardmarks[player_move] = current_player

board = []

## Display Board with selections that players have made
def display_board():
    board.clear()
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