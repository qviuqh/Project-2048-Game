import numpy as np
from Board_game import random_tile

def merge_tiles(row):
    new_row = np.zeros(4, dtype = int)
    index = 0
    for value in row:
        if value != 0:
            if new_row[index] == 0:
                new_row[index] = value
            elif new_row[index] == value:
                new_row[index] *= 2
                index += 1
            else:
                index += 1
                new_row[index] = value
    return new_row

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
    
    random_tile(board)
    return board