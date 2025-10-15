import time
import random
from typing import Any, List, Tuple




def play(board:List[List[int]], choices:List[int], player:int, memory:Any) -> Tuple[int, Any]:
    start_time = time.perf_counter()

    if memory is None:
        memory = {
            'total_time_ms': 0.0,
            'turns': 0,
            'target_avg_ms': 0.02 
        }
    run_strategic_logic = True
    if memory['turns'] > 3:
        current_avg_ms = memory['total_time_ms'] / memory['turns']
        if current_avg_ms > memory['target_avg_ms']:
            run_strategic_logic = False

    move = -1

    if run_strategic_logic:
       
        board_size = len(board)
        opponent = 1 if player == 0 else 0
        block_move = -1

        for col in choices:

            board[col].append(player)
            if check_win_at_position(board, col, player, board_size):
                board[col].pop()
                move = col
                break
            board[col].pop()

           
            if block_move == -1:
                board[col].append(opponent)
                if check_win_at_position(board, col, opponent, board_size):
                    block_move = col
                board[col].pop()
        
        if move == -1 and block_move != -1:
            move = block_move

    if move == -1:
        move = random.choice(choices)

    end_time = time.perf_counter()
    turn_duration_ms = (end_time - start_time) * 1000
    memory['total_time_ms'] += turn_duration_ms
    memory['turns'] += 1

    return move, memory

def check_win_at_position(board: List[List[int]], col: int, player: int, board_size: int) -> bool:
    row = len(board[col]) - 1
    if row >= 2 and board[col][row-1] == player and board[col][row-2] == player:
        return True
    for dx, dy in [(1, 0), (1, 1), (1, -1)]:
        count = 1
        for i in range(1, 3):
            c, r = col + i * dx, row + i * dy
            if 0 <= c < board_size and 0 <= r < len(board[c]) and board[c][r] == player:
                count += 1
            else: break
        for i in range(1, 3):
            c, r = col - i * dx, row - i * dy
            if 0 <= c < board_size and 0 <= r < len(board[c]) and board[c][r] == player:
                count += 1
            else: break
        if count >= 3:
            return True
    return False
