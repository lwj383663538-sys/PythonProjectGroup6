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

    # 1. Start Strong: If you are the first player (X), 5

    # place your mark in a corner. 
    # This move opens up multiple winning paths and puts pressure on your opponent to respond correctly. 
    # If your opponent does not place their O in the center, you can often secure a win. 

    # 2.
    # Control the Center: If you are the second player (O), 
    # try to take the center square if your opponent starts in a corner. 
    # This position allows you to block their potential winning moves while creating your own opportunities. 
     length_board = len(board)
     

     if not board:
         turn = 0
     else:
         turn = sum(1 for sublist in board for item in sublist if item is not None)
     
     chosen_move = None
     
     if turn == 0:
       chosen_move = 0
     elif turn == 1:
       chosen_move = length_board//2
     else:
        for choice in choices:
           best_choice = 



     print(f'Player variable: {player}')
     print(f'Turn variable: {turn}')
     print(f'Board variable: {board}')
     print(f'Choices variable: {choices}')
     print(f'Memory variable: {memory}')
     print(f'Chosen move variable: {chosen_move}')

     if not memory:
        memory =  []
        memory.append(chosen_move)
     else:
        memory.append(chosen_move)
    
     if chosen_move == None:
        chosen_move = 1
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

    # Stella

    # 5.
    # Force a Draw: If both players play optimally, 
    # the game will end in a draw. If you find yourself in a position where you cannot win, 
    # focus on blocking your opponent's moves to ensure the game does not end in a loss. 

    # Nuoting

    # Simon tries all of them 

     return chosen_move,  memory
