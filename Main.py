from pynput.keyboard import Listener
import numpy as np
import random

#Random Tile
population  = [2, 4]
probability = [0.8, 0.2]

#New board game
def new_board():
    board_game = np.zeros((4, 4), dtype = int)
    for _ in range(2):
        random_title(board_game)
    return board_game

def random_title(board):
    empty_cells = list(zip(*np.where(board == 0)))
    if empty_cells:
        i, j = random.choice(empty_cells)
        new_title = random.choices(population, probability)
        board[i, j] = new_title[0]

def merge_tiles(row):
    new_row = np.zeros(4, dtype=int)
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
    
    random_title(board)
    return board

#Create new board game
Board = new_board()
print(Board)

def keypress(key):
    global Board
    if str(key) == 'Key.esc':
        raise SystemExit(0)
    elif str(key) == "Key.right":
        direction = "right"
        Board = move(Board, direction)
        print(Board)
    elif str(key) == "Key.left":
        direction = "left"
        Board = move(Board, direction)
        print(Board)
    elif str(key) == "Key.up":
        direction = "up"
        Board = move(Board, direction)
        print(Board)
    elif str(key) == "Key.down":
        direction = "down"
        Board = move(Board, direction)
        print(Board)
    
    print('_______________')
    #print(key)
with Listener(on_press = keypress) as listener:
    listener.join()