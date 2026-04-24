import random

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

## Conditionals to determine the state of the game
winning_combinations = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,5,9],
    [1,4,7],
    [2,5,8],
    [3,6,9]
]

move_log = {
    'X': [1,2,3],
    'O': []
}

game_over_flag = False

## When new game starts, randomly pick which player gets to go first
current_player = players[random.randrange(0,2)]

## Update Board with the selection that the current player has made
player_move = int(input(f"What is {current_player}'s move? (1-9))"))
boardmarks[player_move] = current_player
move_log[current_player].append(player_move)

## Once when mark has been stored, set the current player
current_player = [player for player in players if player != current_player]

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

## Logic to persist game until either player reaches a winning combination/game is a tie
## while game_over_flag == False:
##    print('Test!!!')
##    game_over_flag = True

for key in move_log:
    for combination in winning_combinations:
        print(move_log[key], combination)
        if combination == move_log[key]:
            print('Winning combination!')
        else:
            print('Not a winning combination!')

## print(''.join(display_board()))
## print(current_player)
## print(move_log)