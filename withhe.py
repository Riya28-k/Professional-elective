import math

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

def evaluate(board):
    if check_winner(board,"O"):
        return +1
    elif check_winner(board,"X"):
        return -1
    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score != 0 or is_full(board):
        return score

    if is_maximizing:  # AI's turn (O)
        best = -math.inf
        for i in range(9):
            if board[i]==" ":
                board[i]="O"
                best = max(best, minimax(board, depth+1, False))
                board[i]=" "
        return best
    else:  # Human's turn (X)
        best = math.inf
        for i in range(9):
            if board[i]==" ":
                board[i]="X"
                best = min(best, minimax(board, depth+1, True))
                board[i]=" "
        return best

def best_move(board):
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i]==" ":
            board[i]="O"
            move_val = minimax(board, 0, False)
            board[i]=" "
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def play_game():
    board = [" "]*9

    while True:
        print_board(board)
        move = int(input("Enter position (0-8): "))
        if board[move]!=" ":
            print("Invalid move!")
            continue
        board[move]="X"

        if check_winner(board,"X"):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move = best_move(board)
        board[ai_move]="O"
        print(f"AI chooses {ai_move}")

        if check_winner(board,"O"):
            print_board(board)
            print("AI wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

play_game()
