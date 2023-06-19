import random

BOARD_GAME_SIZE = 20

def evaluate(tic_tac_toe_string):
    'Function that evaluates the tic-tac-toe string and returns the state of the game'
    if "xxx" in tic_tac_toe_string: 
        return "x" # player who uses xs wins
    elif "ooo" in tic_tac_toe_string:
        return "o" # player who uses os wins
    elif "-" not in tic_tac_toe_string:
        return "!" # draw
    else:
        return "-" # game continues
    
def move(board, mark, position):
    'Returns the game board with the given mark in the given position.'
    new_board = board[:(position)] + mark + board[(position + 1):]
    return new_board

def player_move(tic_tac_toe_string):
  while True:
    position = int(input("Which position do you want to play? Input a number from 0 to " + str(BOARD_GAME_SIZE - 1) + ": "))
    if position > BOARD_GAME_SIZE - 1 or tic_tac_toe_string[position] != "-":
      print("Wrong input, please try again")    
    else:
      string_after_player_move = move(tic_tac_toe_string, "x", position)
      return string_after_player_move
    

def pc_move(tic_tac_toe_string):
  "Returns a game board with the computer's move."
  while True:
    if(tic_tac_toe_string.count("-") == 0):
       return tic_tac_toe_string
    computer_position = random.randrange(BOARD_GAME_SIZE)
    if tic_tac_toe_string[computer_position] == "-":
      string_after_pc_move = move(tic_tac_toe_string, "o", computer_position)
      return string_after_pc_move

def tictactoe():
  "Tictactoe game function"
  tic_tac_toe_string = ""
  for i in range(BOARD_GAME_SIZE):
    tic_tac_toe_string += "-"
  while evaluate(tic_tac_toe_string) == "-":
    tic_tac_toe_string = player_move(tic_tac_toe_string)
    print(tic_tac_toe_string)
    tic_tac_toe_string = pc_move(tic_tac_toe_string)
    print(tic_tac_toe_string)
  if evaluate(tic_tac_toe_string) == "x":
    print("Congrats, you won!")
  elif evaluate(tic_tac_toe_string) == "!":
    print("It's  draw")
  else:
    print("Computer won, sorry")

tictactoe()
