from pynput.keyboard import Listener
import numpy as np
import random

#Random Tile
population  = [2, 4]
probability = [0.8, 0.2]

#Create a game table
Matrix =  np.array([[0, 0, 0, 0], 
                    [0, 0, 0, 0], 
                    [0, 0, 0, 0], 
                    [0, 0, 0, 0]])

valid_pos   =  [[0, 0], [0, 1], [0, 2], [0, 3],
                [1, 0], [1, 1], [1, 2], [1, 3],
                [2, 0], [2, 1], [2, 2], [2, 3],
                [3, 0], [3, 1], [3, 2], [3, 3]]
storage_pos = []

for i in range(1,3):
    pos = random.choice(valid_pos)
    valid_pos.remove(pos)
    storage_pos.append(pos)
    New_tile = random.choices(population, probability)
    Matrix[pos[0]][pos[1]] = New_tile[0]

print(Matrix)

def keypress(key):
    if str(key) in ["Key.right", "Key.left", "Key.up", "Key.down"]:
        print(random.choices(population, probability), end = '')
    elif str(key) == 'Key.esc':
        raise SystemExit(0)
    print(key)

with Listener(on_press = keypress) as listener:
    listener.join()