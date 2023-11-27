import numpy as np
import Score

# Check valid move
def valid_move(board, direction):
    test_valid = np.copy(board)
    test_valid = move(test_valid, direction)
    Checking = test_valid == board
    if np.any(Checking == False):
        return True
    else:
        return False

# Checking gameover
def Game_over(board):
    global Score
    directions = ["up", "down", "left", "right"]
    
    for d in directions:
        if np.any(board == 0) or valid_move(board, d):
            return False
    
    if Score.new_score > Score.high_score:
        Score.update_high_score(Score.new_score)
    return True


# Merge row or col
def merge_tiles(row):
    global Score
    new_row = np.zeros(4, dtype = int)
    index = 0
    for value in row:
        if value != 0:
            if new_row[index] == 0:
                new_row[index] = value
            elif new_row[index] == value:
                Score.new_score += new_row[index]
                new_row[index] *= 2
                index += 1
            else:
                index += 1
                new_row[index] = value
    return new_row


# Moving in board
def move_left(board):
    return np.apply_along_axis(merge_tiles, 1, board)

def move_right(board):
    return np.apply_along_axis(lambda row: merge_tiles(row[::-1])[::-1], 1, board)

def move(board, direction):
    if direction == "up":
        board = np.transpose(board)
        board = move_left(board)
        board = np.transpose(board)
    elif direction == "down":
        board = np.transpose(board)
        board = move_right(board)
        board = np.transpose(board)
    elif direction == "left":
        board = move_left(board)
    elif direction == "right":
        board = move_right(board)
    
    return board