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
     board_size = len(board)
     turn = sum(len(col) for col in board)
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
            test_board = [col.copy() for col in board] 
            test_board[col].append(player)
            if check_if_player_wins(test_board, player, board_size, win_length):
                return col, memory  # Check if we have an immediate winning opportunity
     for win_length in win_lengths:
        for col in choices:  # Check each possible move to see if opponent would win by playing there
    # Create a temporary board for testing
            test_board = [col.copy() for col in board]
            test_board[col].append(opponent)
            if check_if_player_wins(test_board, opponent, board_size, win_length):  
                return col, memory  # If op would win, we must block! Choose this position
    
    # make winning move if available
     for col in choices:
        test_board = [col[:] for col in board]
        test_board[col].append(player)
        if count_winning_moves(test_board, player, board_size) >= 1:
            return col, memory
    
    #check for next step defense
     for col in choices:
        test_board = [col[:] for col in board]
        test_board[col].append(opponent)
        if count_winning_moves(test_board, opponent, board_size) >= 1:
            return col, memory
        
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
        # Check diagonal (top-left to bottom-right)
            diag1_score = 1
            # left up
            r, c = row_position - 1, col - 1
            while r >= 0 and c >= 0 and r < len(board[c]) and board[c][r] == player:
                diag1_score += 1
                r -= 1
                c -= 1
            # right down
            r, c = row_position + 1, col + 1
            while r < board_size and c < len(board) and r < len(board[c]) and board[c][r] == player:
                diag1_score += 1
                r += 1
                c += 1
        # Check diagonal (top-right to bottom-left)
            diag2_score = 1
            # right up
            r, c = row_position - 1, col + 1
            while r >= 0 and c < len(board) and r < len(board[c]) and board[c][r] == player:
                diag2_score += 1
                r -= 1
                c += 1
            # left down
            r, c = row_position + 1, col - 1
            while r < board_size and c >= 0 and r < len(board[c]) and board[c][r] == player:
                diag2_score += 1
                r += 1
                c -= 1

            current_streak = max(vertical_streak, horizontal_streak, diag1_score, diag2_score)  # Take the maximum streak count
            if current_streak > max_streak:
                max_streak = current_streak
                best_col = col
        if best_col is not None and max_streak >= 2:  # If found a position that can form longer consecutive pieces
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
      return False

def count_winning_moves(board, player, board_size):
    #Count the number of winning moves available to the player
    winning_moves = 0
    empty_cols = [col for col in range(board_size) if len(board[col]) < board_size]
    for col in empty_cols:
        test_board = [col[:] for col in board]
        test_board[col].append(player)
        # Check all possible winning lengths
        for win_length in range(3, min(board_size, 5) + 1):
            if check_if_player_wins(test_board, player, board_size, win_length):
                winning_moves += 1
                break
    return winning_moves