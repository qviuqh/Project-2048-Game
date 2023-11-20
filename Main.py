from pynput.keyboard import Listener
import Move
import Board_game

#Create new board game
Board = Board_game.new_board()
print(Board)
print()

def keypress(key):
    global Board
    
    if str(key) not in ["Key.esc", "Key.right", "Key.left", "Key.up", "Key.down"]:
        pass
    else:
        if Move.Game_over(Board):
            print("Game Over")
            raise SystemExit(0)
    
        if str(key) == "Key.esc":
            raise SystemExit(0)
        elif str(key) == "Key.right":
            direction = "right"
        elif str(key) == "Key.left":
            direction = "left"
        elif str(key) == "Key.up":
            direction = "up"
        elif str(key) == "Key.down":
            direction = "down"

        if Move.valid_move(Board, direction) == True:
            Board = Move.move(Board, direction)
            Board_game.random_tile(Board)

        print(Board)
        print()

with Listener(on_press = keypress) as listener:
    listener.join()