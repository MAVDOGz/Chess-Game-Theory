import copy
 
def gameOver(utility):

    if utility == 1:
        print("Utility: ", utility)
        print("Checkmate! Black Wins!")
    elif utility == -1:
        print("Utility: ", utility)
        print("Checkmate! White Wins!")
    elif utility == float('inf') or utility == float('-inf'):
        print("Utility: ", 0)
        print('Stalemate!')
    else:
        print("Utility: ", 0)
        print("Max Depth Reached / Tie")
        
def checkTest(chessboard):
    # Assuming chessboard has a property currMove, and blackCheck, whiteCheck are instance variables
    chessboard.blackCheck = False
    chessboard.whiteCheck = False
    if chessboard.player == 0:
        kingRow = chessboard.blackPieces['Kb'].row
        kingCol = chessboard.blackPieces['Kb'].col
        # print('king coords: ', kingRow, kingCol)
                    
        for piece, obj in chessboard.whitePieces.items():
            if (kingRow,kingCol) in obj.checkMoves(chessboard):
                # print(obj)
                chessboard.blackCheck = True          
            
    else:
        kingRow = chessboard.whitePieces['Kw'].row
        kingCol = chessboard.whitePieces['Kw'].col

        for piece, obj in chessboard.blackPieces.items():
            if (kingRow, kingCol) in obj.checkMoves(chessboard):
                chessboard.whiteCheck = True  
                                
def simulate(chessboard, piece, move):

    newChessboard = copy.deepcopy(chessboard) # copy the board
    movePiece = newChessboard.pieces[piece] # get the piece object
    isCapture = False
    
    # remove the movePiece from current cell
    newChessboard.board[movePiece.row][movePiece.col].remove()
        
    # capture?
    if newChessboard.board[move[0]][move[1]].piece is not None:
        captured = newChessboard.board[move[0]][move[1]].piece
        isCapture = True
        if newChessboard.player == 0:
            del newChessboard.whitePieces[captured.id]                    
        else:
            del newChessboard.blackPieces[captured.id]

    # move the piece
    newChessboard.board[move[0]][move[1]].set(movePiece)  
    
    # update piece attributes
    movePiece.row = move[0]
    movePiece.col = move[1]
    
    # update depth
    newChessboard.depth += 1  # Increment depth
    
    # check for tie moves
    if isCapture == False:
        newChessboard.nonCaptureMoves += 1
    else:
        newChessboard.nonCaptureMoves = 0
    
    return newChessboard   
    
#################################   

def backward_induction(chessboard, maxDepth):
    legalMoves = chessboard.generate_legal_moves()
    max_utility = float('-inf')
    min_utility = float('inf')
    best_sequence = []
    
    # chessboard.print()
    # print(legalMoves)

    checkTest(chessboard)

    if chessboard.player == 1 and not legalMoves:
        if chessboard.whiteCheck:
            chessboard.whitePieces['Kw'].mated = True
            return 1, [(None, None, chessboard)]
        else:
            return max_utility, [(None, None, chessboard)]
        
    elif chessboard.player == 0 and not legalMoves:
        if chessboard.blackCheck:
            chessboard.blackPieces['Kb'].mated = True
            return -1, [(None, None, chessboard)]
        else:
            return min_utility, [(None, None, chessboard)]
        
    elif chessboard.depth >= maxDepth or chessboard.nonCaptureMoves > 2:
        return 0, [(None, None, chessboard)]
    
    else:
        if chessboard.player == 0:  # Black's turn
            for piece in legalMoves:
                for move in legalMoves[piece]:
                    new_board = simulate(chessboard, piece, move)
                    new_board.player = 1  # Switch player
                    utility, recursive_sequence = backward_induction(new_board, maxDepth)
                    if utility > max_utility:
                        max_utility = utility
                        best_sequence = [(piece, move, new_board)] + recursive_sequence
            return max_utility, best_sequence
        elif chessboard.player == 1:  # White's turn
            for piece in legalMoves:
                for move in legalMoves[piece]:
                    new_board = simulate(chessboard, piece, move)
                    new_board.player = 0  # Switch player
                    utility, recursive_sequence = backward_induction(new_board, maxDepth)
                    if utility < min_utility:
                        min_utility = utility
                        best_sequence = [(piece, move, new_board)] + recursive_sequence
            return min_utility, best_sequence

def print_sequence(sequence):
    for step in sequence:
        piece, move, board = step
        print(f"Move {piece} to {move}:")
        print()
        board.print()
    
def calcBoardVal(chessboard):

    val = 0
    blackVal = 0
    blackRisk = 0
    blackCover = 0
    whiteVal = 0
    whiteRisk = 0
    whiteCover = 0
    # print(obj.id, ":",move)    
           
    # values of black
    for own, blackPiece in chessboard.blackPieces.items():
        blackVal += blackPiece.val
        # calc self risk
        for opp, whitePiece in chessboard.whitePieces.items():
            if (blackPiece.row, blackPiece.col) in whitePiece.checkMoves(chessboard):
                # print(opp, own, ownPiece.val*.5)
                blackRisk += blackPiece.val*.5
        # calc cover
        for own2, blackPiece2 in chessboard.blackPieces.items():
            if (blackPiece2 != blackPiece):
                if (blackPiece.row, blackPiece.col) in blackPiece2.checkMoves(chessboard):
                    blackCover += blackPiece.val*.5
 
    # values of opponent team
    for opp, whitePiece in chessboard.whitePieces.items(): 
        whiteVal += whitePiece.val
        # calc opp Risk
        for own, blackPiece in chessboard.blackPieces.items():
            if (whitePiece.row, whitePiece.col) in blackPiece.checkMoves(chessboard):
                whiteRisk += whitePiece.val*.5
        # calc cover
        for opp2, whitePiece2 in chessboard.whitePieces.items():
            if (whitePiece2 != whitePiece):
                if (whitePiece.row, whitePiece.col) in whitePiece2.checkMoves(chessboard):
                    whiteCover += whitePiece.val*.5            
                
    ### sum
    val = (blackVal + blackCover + whiteRisk) - (whiteVal + whiteCover + blackRisk)
    return val
       
        
