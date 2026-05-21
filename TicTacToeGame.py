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
    [3,6,9],
    [3,5,7]
]

move_log = {
    'X': [[],[],[],[],[],[],[]],
    'O': [[],[],[],[],[],[],[]]
}

game_over_flag = False

## When new game starts, randomly pick which player gets to go first
current_player = players[random.randrange(0,2)]
current_player_string = "".join(current_player)

## Keep a log of all moves that each player has made
def log_player_moves(log, winning_combinations):
    for moves, winning_combo in zip(log, winning_combinations):
        if player_move in winning_combo:
            moves.append(player_move)
        else:
            return
        moves.sort()
    
board = []

## Display Board with selections that players have made
def display_board():
    board.clear()
    indices = [2,5,8]
    for key in boardmarks:
        if key in [3,6,9]:
            board.append(f'{boardmarks[key]}\n-+-+-\n')
        else:
            board.append(f'{boardmarks[key]}|')
    return board

## Determine if any possible moves made by the player matches with any of the winning combinations
def determine_winner(current_player_moves, winning_combinations):
    for value, winning_combo in zip(current_player_moves,winning_combinations):
        if value == winning_combo:
            return True
        else:
            return False

## Logic to persist game until either player reaches a winning combination/game is a tie
while game_over_flag == False:
    ## Update Board with the selection that the current player has made
    player_move = int(input(f"What is {current_player_string}'s move? (1-9))"))
    if boardmarks[player_move] != ' ':
        print('Invalid move!')
    else:
        boardmarks[player_move] = current_player_string

    ## Display Board
    print(''.join(display_board()))
    
    ## Log the move the current player has made
    log_player_moves(move_log[current_player_string], winning_combinations)

    ## Determine if the player has made a winning combination
    game_over_flag = determine_winner(move_log[current_player_string], winning_combinations)

    ## Once when mark has been stored, set the current player
    current_player = [player for player in players if player != current_player_string]
    current_player_string = "".join(current_player)