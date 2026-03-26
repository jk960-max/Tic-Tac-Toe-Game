def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")

def main():
    print("Welcome to Tic Tac Toe!")

    if __name__ == "__main__":
        play_game()



def check_winner(board):
    winning_combinations = [
        (0,1,2), (3,4,5), (6,7,8), # Rows
        (0,3,6), (1,4,7), (2,5,8), # Columns
        (0,4,8), (2,4,6) # Diagonals
    ]

    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != " ":
            return True

        return False

def play_game():
        board = [" "] * 9
        current_player = "X"


        while True:
            print_board(board)

            # CHECK WIN HERE
            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            try:
                move = int(input(f"Player {current_player}, choose position (0-8): "))
            except ValueError:
                print("Invalid input. Please try again. Enter a number between 0 and 8.")
                continue

            if move < 0 or move > 8:
                print("Invalid position! Choose 0-8.")
                continue

            if board[move] != " ":
                print("The spot is already occupied. Choose another spot.")
                continue

            board[move] = current_player


            #THEN check tie
            if " " not in board:
                print_board(board)
                print("It's a tie!")
                break

            # THEN switch player
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
        main()


