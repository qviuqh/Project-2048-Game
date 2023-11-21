Storage_board = []
Storage_score = []

def add_storage(board, score):
    global Storage_board
    global Storage_score
    
    Storage_board.append(board)
    Storage_score.append(score)

def redu():
    global Storage_board
    global Storage_score
    
    Storage_board.pop(len(Storage_board) - 1)
    board = Storage_board[len(Storage_board) - 1]
    
    score = Storage_score[len(Storage_score) - 1]
    Storage_score.pop(len(Storage_score) - 1)
    
    return board, score