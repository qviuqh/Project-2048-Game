import numpy as np
import random

# Tile
population  = [2, 4]
probability = [0.8, 0.2]

# New board game
def new_board():
    board_game = np.zeros((4, 4), dtype = int)
    for _ in range(2):
        random_tile(board_game)
    return board_game

def random_tile(board):
    empty_cells = list(zip(*np.where(board == 0)))
    if empty_cells:
        i, j = random.choice(empty_cells)
        new_tile = random.choices(population, probability)
        board[i, j] = new_tile[0] 