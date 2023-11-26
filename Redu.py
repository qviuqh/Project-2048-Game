Storage_board = []
Storage_score = []

def add_storage(board, score):
    global Storage_board
    global Storage_score
    if len(Storage_board) < 6:
        Storage_board.append(board)
    else:
        Storage_board.pop(0)
        Storage_board.append(board)
    
    if len(Storage_score) < 6:
        Storage_score.append(score)
    else:
        Storage_score.pop(0)
        Storage_score.append(score)
    

def redu():
    global Storage_board
    global Storage_score
    
    Storage_board.pop(len(Storage_board) - 1)
    board = Storage_board[len(Storage_board) - 1]
    
    Storage_score.pop(len(Storage_score) - 1)
    score = Storage_score[len(Storage_score) - 1]
    
    return board, score