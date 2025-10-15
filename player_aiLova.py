#====================================================================================================#
# Imports:                                                                                           #
#====================================================================================================#

import random
from typing import Any, List, Tuple

#====================================================================================================#
# Play Function:                                                                                     #
#====================================================================================================#
def play(board:List[List[int]], choices:List[int], player:int, memory:Any) -> Tuple[int, Any]:
    '''Plays random moves.
    
        Arguments:
            board (List[List[int]]): the game plan as a list of columns. Each column is a list of integer ids signifying the player who placed the piece.
            choices     (List[int]): the possible moves allowed by the game rules.
            player            (int): integer id of the current player in the game plan.
            memory            (any): persistent information passed as the second output in the previous round. Initialized with None.

        Returns   (Tuple[int, Any]): A tuple of the selected column (int) and the memory object for the next iteration (can be anything).
    '''

 # 3.
    # Create Forks: A fork is a position where you create two winning opportunities at once. 
    # For example, if you have two X's in a row and your opponent can only block one, 
    # you will win on your next turn. Always look for ways to set up a fork.  
    
    ## The code: 
    ### The code only looks vertically in each column to see
    ## how many if its own pieces are stacked. The Ai chooses
    ## the column with the most pieces in a row.
    ## We could also check horizontal or diagonal, 
    ## but that was way to complicated for me.

    best_col = choices[0]   # we start with first column in choices
    best_score = -1         # Start vaule

    ## we check all columns in choices, one by one
    for col in choices: 
        vertical_count = 0 # Start value 0
        current_height = len(board[col])  # check the length of the board, example 3x3 gives current_height = 3 

        ## Count our pieces stacked at the top of this column
        for i in reversed(range(current_height)): 
            if board[col][i] == player: 
                vertical_count += 1 
            else: 
                break ## stop counting if it's not our piece
        
        vertical_count += 1 ## add the piece we are about to place

        ####### To Check what happens during run # REMOVE this later
        print(f"Checking column {col}")
        print(f"Current height: {current_height}")
        print(f"Vertical count if we place here: {vertical_count}")
        print(f"Current best_score: {best_score}, best_col: {best_col}")
        #######

    
    ## find the column with the highest count
        if vertical_count > best_score:
            best_score = vertical_count
            best_col = col

    ## return the column to play and the memory 
    return best_col, memory
        
