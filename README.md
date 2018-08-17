# Battleship
#A prelude to a simple game.

from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
  print "Turn ",turn+1
  
  guess_row=int(raw_input("guess row: "))
  guess_col=int(raw_input("Guess col: "))
  
  if guess_row==ship_row and guess_col==ship_col:
    print "Congratulations! You sank my ship!"
    break
  else:
      if (guess_row<0 and guess_row>4) or (guess_col<0 or guess_col>4):
        print "Oops! That's not even in the ocean!"
      elif board[guess_row][guess_col]=='X':
        print "You've guesses that already"
      else :
        print "Sorry! That's a wrong guess"
        board[guess_row][guess_col]='X'
        if(turn==3):
          print "Game Over"
          break
        
        print_board(board)
        
