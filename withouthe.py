import random

def print_board(board):
    for i in range(3):
        print(board[3*i:3*(i+1)])
    print()

def check_winner(board, player):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8], # rows
        [0,3,6],[1,4,7],[2,5,8], # cols
        [0,4,8],[2,4,6]          # diagonals
    ]
    return any(all(board[pos]==player for pos in line) for line in win_states)

def is_full(board):
    return all(x != " " for x in board)

def play_game():
    board = [" "]*9
    players = ["X","O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn%2]

        if player == "X":  # Human
            move = int(input("Enter position (0-8): "))
        else:  # Random move for computer
            move = random.choice([i for i in range(9) if board[i]==" "])

        if board[move] != " ":
            print("Invalid move!")
            continue

        board[move] = player

        if check_winner(board, player):
            print_board(board)
            print(f"{player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1

play_game()
