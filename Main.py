from pynput.keyboard import Listener
import Score
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
        
        print("High Score:", Score.high_score)
        print("Score:", Score.new_score)
        print('-----------------------')
        print(Board)
        print()

def keyReleased(key):
    if Move.Game_over(Board):
        print("Game Over")
        raise SystemExit(0)

with Listener(on_press = keypress, on_release = keyReleased) as listener:
    listener.join()

#if Move.Game_over(Board):
#    print("Game Over")
#    raise SystemExit(0)