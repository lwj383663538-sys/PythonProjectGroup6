#====================================================================================================#
# Imports:                                                                                           #
#====================================================================================================#
import random
from typing import Any, List, Tuple

#====================================================================================================#
# Play Function:                                                                                     #
#====================================================================================================#


def play(board:List[List[int]], choices:List[int], player:int, memory:Any) -> Tuple[int, Any]:    
     '''Your team's player.                                                                        
                                                                                                   
         Arguments:                                                                                
             board (List[List[int]]): The game plan as a list of columns. Each column is a list of 
                                      integer ids signifying the player who placed the piece.      
             choices     (List[int]): The possible moves allowed by the game rules.                
             player            (int): Integer id of the current player in the game plan.           
             memory            (any): Persistent information passed as the second output in the    
                                      previous round. Initialized with None.                       
                                                                                                   
         Returns   (Tuple[int, Any]): A tuple of the selected column (int) and the memory object   
                                      for the next iteration (can be anything).                    
     '''                                                                                           
     
     # your code goes here:   

    # 1. Start Strong: If you are the first player (X), 
    # place your mark in a corner. 
    # This move opens up multiple winning paths and puts pressure on your opponent to respond correctly. 
    # If your opponent does not place their O in the center, you can often secure a win. 

    # 2.
    # Control the Center: If you are the second player (O), 
    # try to take the center square if your opponent starts in a corner. 
    # This position allows you to block their potential winning moves while creating your own opportunities. 
    #length_board = len(board)
     
    #turn = sum(1 for sublist in board for item in sublist if item is not None)
     

    #  print(f'Board variable: {board}')
    #  print(f'Choices variable: {choices}')
    #  print(f'Player variable: {player}')
     
    #  choices = []
    #  if player == 0:
    #    choices.append(0)
    #  else:
    #      choices.append(length_board//2)

    #  memory = choices
    #  print(choices[0])

     
    #print(memory)
    # 3.
    # Create Forks: A fork is a position where you create two winning opportunities at once. 
    # For example, if you have two X's in a row and your opponent can only block one, 
    # you will win on your next turn. Always look for ways to set up a fork. 

    # Lova

    # 4.
    # Block Your Opponent: If your opponent has two in a row, 
    # you must block their next move to prevent them from winning. 
    # Always be aware of their potential winning paths and respond accordingly. 

     board_size = len(board)
     turn = sum(1 for sublist in board for item in sublist if item is not None)
     print(f'Turn variable: {turn}')
     if turn == 0:
       return 0, memory
     if turn == 1:
         return board_size//2, memory
     if player == 0: # Step 1: Identify the opponent
         opponent = 1
     else:
         opponent = 0 
     win_lengths = [11, 10, 9, 8, 7, 6, 5, 4, 3]
     for win_length in win_lengths:
        for col in choices:
            test_board = []
            for i in range(len(board)):
                test_board.append(board[i][:])
            if col < len(test_board):
                test_board[col] = test_board[col][:]
                test_board[col].append(player)
                if check_if_player_wins(test_board, player, board_size, win_length):
                    print(f'Attack!')
                    return col, memory  # Check if we have an immediate winning opportunity
     for win_length in win_lengths:
        for col in choices:  # Check each possible move to see if opponent would win by playing there
            test_board = []    # Create a temporary board for testing
            for i in range(len(board)):
                test_board.append(board[i][:])  # Copy each column
            if col < len(test_board):
                test_board[col] = test_board[col][:]
                test_board[col].append(opponent)  # Simulate opponent making a move in this column
                if check_if_player_wins(test_board, opponent, len(board), win_length):
                    print(f'Block!')    
                    return col, memory  # If opponent would win, we must block! Choose this position
     if choices:  # Check for positions that can form the longest consecutive pieces
        best_col = None
        max_streak = 0
        for col in choices: # Simulate placing a piece in this column
            row_position = len(board[col]) # Position where new piece will land
            vertical_streak = 1  # Check vertical streak, The new piece itself
            for i in range(1, row_position + 1):  # Check downward (pieces below it)
                if row_position - i >= 0 and board[col][row_position - i] == player:
                    vertical_streak += 1
                else:
                    break
            horizontal_streak = 1  # Check horizontal streak
            left_streak = 0  # Check left
            c = col - 1
            while c >= 0 and row_position < len(board[c]) and board[c][row_position] == player:
                left_streak += 1
                c -= 1
            right_streak = 0 # Check right
            c = col + 1
            while c < len(board) and row_position < len(board[c]) and board[c][row_position] == player:
                right_streak += 1
                c += 1
            horizontal_streak = 1 + left_streak + right_streak
            current_streak = max(vertical_streak, horizontal_streak)  # Take the maximum streak count
            if current_streak > max_streak:
                max_streak = current_streak
                best_col = col
        if best_col is not None and max_streak >= 2:  # If found a position that can form longer consecutive pieces
            print(f'Best Move!')
            return best_col, memory
        
        return random.choice(choices), memory # If no opportunities, choose randomly
     return 0, memory # safe return if no choices available

def check_if_player_wins(board: List[List[int]], check_player: int, board_size: int, win_length: int) -> bool:
      for row in range(board_size):  # Check horizontal direction (rows)
        for col in range(board_size - win_length + 1): # first column to start checking
            all_same = True
            for i in range(win_length): # check next 3 in the row
                current_col = col + i
                if (row >= len(board[current_col]) or 
                    board[current_col][row] != check_player):
                    all_same = False
                    break
            if all_same:
                return True
      for col in range(board_size):  # Check vertical direction (columns)
        if len(board[col]) >= win_length:
            for start_row in range(len(board[col]) - win_length + 1):
                all_same = True
                for i in range(win_length):
                    current_row = start_row + i
                    if board[col][current_row] != check_player:
                        all_same = False
                        break
                if all_same:
                    return True
      for start_col in range(board_size - win_length + 1):  # Check diagonal (top-left to bottom-right)
        for start_row in range(board_size - win_length + 1):
            all_same = True
            for i in range(win_length):
                col_idx = start_col + i
                row_idx = start_row + i
                if (row_idx >= len(board[col_idx]) or 
                    board[col_idx][row_idx] != check_player):
                    all_same = False
                    break
            if all_same:
                return True
      for start_col in range(win_length - 1, board_size): # Check diagonal (top-right to bottom-left)
        for start_row in range(board_size - win_length + 1):
            all_same = True
            for i in range(win_length):
                col_idx = start_col - i
                row_idx = start_row + i
                if (row_idx >= len(board[col_idx]) or 
                    board[col_idx][row_idx] != check_player):
                    all_same = False
                    break
            if all_same:
                return True
      return False

# Check if opponent can win in the next move and block


  # opponent = 3 - player_ai
  # for choices in self.get_available_moves():
  #           temp_board = self.board.copy()
  #           row = self.get_next_available_row(col)
  #           if row is not None:
  #               temp_board[row][col] = opponent
  #               if self.check_winner_on_board(temp_board, opponent):
  #                   return col

  # for row in range(rows-1, -1, -1):
  #       if new_board[row][col] == 0:
  #           new_board[row][col] = player
  #           return new_board

  # Best_move = None
  # max = len(board) 
  # for choice in choices:
  #   temp_board = board.copy()
  #   #temp_board = play_move(temp_board, choice)
  #   new_max = len(temp_board)
  #   if new_max > max:
  #     max = new_max
  #     Best_move = choice
  # if Best_move is None:
  #   Best_move = random.choice(choices)
  # else:
  #    choice = Best_move

    # Stella

    # 5.
    # Force a Draw: If both players play optimally, 
    # the game will end in a draw. If you find yourself in a position where you cannot win, 
    # focus on blocking your opponent's moves to ensure the game does not end in a loss. 

    # Nuoting

    # Simon tries all of them 
