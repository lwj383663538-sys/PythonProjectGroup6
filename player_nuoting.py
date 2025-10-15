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
    
    board_size = len(board)
    if player == 0: # Step 1: Identify the opponent
        opponent = 1
    else:
        opponent = 0 

    # Step 2: Block immediate opponent win
    for col in choices:  
        test_board = [b[:] for b in board]
        test_board[col].append(opponent)
        if check_if_player_wins(test_board, opponent, len(board)):
            return col, memory  # Block the opponent's win immediately

    # Step 3: Take winning opportunity if available
    for col in choices:
        test_board = [b[:] for b in board]
        test_board[col].append(player)
        if check_if_player_wins(test_board, player, board_size):  
            return col, memory # Take win if possible

    #force a draw
    safe_moves = []
    for col in choices:
        # Test if this move leads to an immediate threat for us
        test_board = [b[:] for b in board]
        test_board[col].append(player)
        opponent_can_win_next = False
        for opp_col in range(len(board)):
            if opp_col in choices:  # Opponent can only play valid columns
                sim_board = [b[:] for b in test_board]
                sim_board[opp_col].append(opponent)
                if check_if_player_wins(sim_board, opponent, board_size):
                    opponent_can_win_next = True
                    break
        if not opponent_can_win_next:
            safe_moves.append(col)
            
    # If there are safe moves that do not give the opponent a chance to win, choose from them
    if safe_moves:
        return random.choice(safe_moves), memory
    
    #code for stella
    if choices: 
        return random.choice(choices), memory 
    return 0, memory # safe return if no choices available


#code from Stella
def check_if_player_wins(board: List[List[int]], check_player: int, board_size: int) -> bool:
      for row in range(board_size):  # Check horizontal direction (rows)
        for col in range(board_size - 2): # first column to start checking
            all_same = True
            for i in range(3): # check next 3 in the row
                current_col = col + i
                if (row >= len(board[current_col]) or 
                    board[current_col][row] != check_player):
                    all_same = False
                    break
            if all_same:
                return True
      for col in range(board_size):  # Check vertical direction (columns)
        if len(board[col]) >= 3:
            for start_row in range(len(board[col]) - 2):
                all_same = True
                for i in range(3):
                    current_row = start_row + i
                    if board[col][current_row] != check_player:
                        all_same = False
                        break
                if all_same:
                    return True
      for start_col in range(board_size - 2):  # Check diagonal (top-left to bottom-right)
        for start_row in range(board_size - 2):
            all_same = True
            for i in range(3):
                col_idx = start_col + i
                row_idx = start_row + i
                if (row_idx >= len(board[col_idx]) or 
                    board[col_idx][row_idx] != check_player):
                    all_same = False
                    break
            if all_same:
                return True
      for start_col in range(2, board_size): # Check diagonal (top-right to bottom-left)
        for start_row in range(board_size - 2):
            all_same = True
            for i in range(3):
                col_idx = start_col - i
                row_idx = start_row + i
                if (row_idx >= len(board[col_idx]) or 
                    board[col_idx][row_idx] != check_player):
                    all_same = False
                    break
            if all_same:
                return True
      return False
