def print_board(board):
    """Function to print the Tic-Tac-Toe board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Function to check if there's a winner"""
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def tic_tac_toe():
    """Function to play Tic-Tac-Toe"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    player_idx = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for _ in range(9):
        row = int(input(f"Player {players[player_idx]}, enter row (0-2): "))
        col = int(input(f"Player {players[player_idx]}, enter column (0-2): "))

        if board[row][col] != " ":
            print("That cell is already occupied. Try again.")
            continue

        board[row][col] = players[player_idx]
        print_board(board)

        if check_winner(board):
            print(f"Player {players[player_idx]} wins!")
            break

        player_idx = (player_idx + 1) % 2
    else:
        print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
