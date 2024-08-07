from funcs import *
import copy
class Knight:
    def __init__(self, row, col, color, id):
        self.row = row
        self.col = col
        self.color = color
        self.val = 3
        self.id = id

    def getMoves(self, chessboard):
        moves = {}
        capMoves = {}
        preCheckBlack = chessboard.blackCheck
        preCheckWhite = chessboard.whiteCheck
        
        for move in self.checkMoves(chessboard):        
            chessboard2=copy.deepcopy(chessboard)
            chessboard2.board[self.row][self.col].remove()
            isCapture = False
            
            if chessboard2.board[move[0]][move[1]].color != self.color:            
                # capture?
                if chessboard2.board[move[0]][move[1]].piece is not None:
                    captured = chessboard2.board[move[0]][move[1]].piece
                    isCapture = True
                    if chessboard2.player == 0:
                        del chessboard2.whitePieces[captured.id]
                    else:
                        del chessboard2.blackPieces[captured.id]
                
                chessboard2.board[move[0]][move[1]].set(self)
                checkTest(chessboard2)
                # chessboard2.print()
                # print(chessboard2.blackCheck)
                if chessboard2.player == 0 and chessboard2.blackCheck == False:
                    if isCapture or (chessboard2.whiteCheck == True):
                        capMoves[move] = calcBoardVal(chessboard2)
                    else:
                        moves[move] = calcBoardVal(chessboard2) 
                   
                elif chessboard2.player == 1 and chessboard2.whiteCheck == False:
                    if isCapture or (chessboard2.blackCheck == True):
                        capMoves[move] = calcBoardVal(chessboard2)
                    else:
                        moves[move] = calcBoardVal(chessboard2)
                        
        if capMoves:
            return True, capMoves
        else:    
            return False, moves
 
    
    def checkMoves(self, chessboard):
        board = chessboard.board

        moves = []
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for dr, dc in knight_moves:
            new_row, new_col = self.row + dr, self.col + dc
            if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                moves.append((new_row, new_col))
        return moves