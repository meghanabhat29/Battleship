from random import randint

def get_new_board(board_size):
    board = []
    for x in range(int(board_size)):
        board.append(["O"] * board_size)
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def check_answer(board,ship_row,ship_col,guess_row,guess_col):
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my ship!")
        return 1
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops! That's not even in the ocean!")
        elif board[guess_row][guess_col] == 'X':
            print("You've guesses that already")
        else:
            print("Sorry! That's a wrong guess")
            board[guess_row][guess_col] = 'X'
        return 0

def main():
    game_board = get_new_board(5)
    print_board(game_board)
    ship_row = random_row(game_board)
    ship_col = random_col(game_board)

    for turn in range(4):
        print("Turn ", turn + 1)
        guess_row = str(input("Guess Row : "))
        guess_col = str(input("Guess column: "))

        if guess_col.isdigit() and guess_row.isdigit():
            answer_value = check_answer(game_board,ship_row,ship_col,guess_row,guess_col)
        else:
            print("Values can only be integer!")

        if(answer_value == 1):
            break
        if (turn == 3):
            print("----- Game Over ----- ")
            break

# Main method where program starts
if __name__ == '__main__':
    main()
