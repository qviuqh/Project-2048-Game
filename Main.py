from pynput.keyboard import Listener
import Move
import Board_game

#Create new board game
Board = Board_game.new_board()
print(Board)
print('_______________')

def keypress(key):
    global Board
    if str(key) == 'Key.esc':
        raise SystemExit(0)
    elif str(key) == "Key.right":
        direction = "right"
        Board = Move.move(Board, direction)
        print(Board)
    elif str(key) == "Key.left":
        direction = "left"
        Board = Move.move(Board, direction)
        print(Board)
    elif str(key) == "Key.up":
        direction = "up"
        Board = Move.move(Board, direction)
        print(Board)
    elif str(key) == "Key.down":
        direction = "down"
        Board = Move.move(Board, direction)
        print(Board)
    
    print('_______________')
    #print(key)
with Listener(on_press = keypress) as listener:
    listener.join()