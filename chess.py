from cell import Cell
from king import King
from queen import Queen
from knight import Knight
from bishop import Bishop
from rook import Rook
from pawn import Pawn
import copy
from funcs import *   

class EasyChessboard1:
    def __init__(self, size=4):
        self.size = size
        self.board = [[Cell() for _ in range(size)] for _ in range(size)]
        self.whiteScore = 0
        self.blackScore = 0
        self.blackCheck = False
        self.whiteCheck = False

        # White pieces
        whiteKing = King(3, 0, 'w', 'Kw')

        self.whitePieces = {
            'Kw': whiteKing,
        }

        # Black pieces
        blackKing = King(0, 3, 'b', 'Kb')
        blackQueen = Queen(0,2, 'b', 'Qb')
        blackRook = Rook (2, 3, 'b', 'Rb')

        self.blackPieces = {
            'Kb': blackKing,
            'Qb': blackQueen,
            'Rb': blackRook
        }
      
        
        # combined pieceSet
        self.pieces = {**self.whitePieces, **self.blackPieces}

        # Place white pieces on the board
        for piece, obj in self.whitePieces.items():
            row, col = obj.row, obj.col
            self.board[row][col].set(obj)

        # Place black pieces on the board
        for piece, obj in self.blackPieces.items():
            row, col = obj.row, obj.col
            self.board[row][col].set(obj)
            
        self.player = 0
        self.nonCaptureMoves = 0
        self.depth = 0
    
    def print(self):
        print('-----------------')
        for row in self.board:
            print(' | '.join(['  ' if cell.piece is None else cell.piece.id[0] + cell.piece.color for cell in row]))
            print('-----------------')
    #################
    def generate_legal_moves(self):
        legalMoves = {}
        selectMoves = {}
        if self.player == 0:
            for piece, obj in self.blackPieces.items():
                capCheck, moves = obj.getMoves(self)
                if capCheck == True:
                    selectMoves[piece] = moves
                else:
                    if moves:
                        legalMoves[piece] = moves
            if selectMoves:
                return selectMoves
            else:
                return legalMoves
                    

        else:
            for piece, obj in self.whitePieces.items():
                capCheck, moves = obj.getMoves(self)
                if capCheck == True:
                    selectMoves[piece] = moves
                else:
                    if moves:
                        legalMoves[piece] = moves
            if selectMoves:
                return selectMoves
            else:
                return legalMoves

class EasyChessboard2:
    def __init__(self, size=4):
        self.size = size
        self.board = [[Cell() for _ in range(size)] for _ in range(size)]
        self.whiteScore = 0
        self.blackScore = 0
        self.blackCheck = False
        self.whiteCheck = False

        # White pieces
        whiteKing = King(3, 0, 'w', 'Kw')
        whiteRook = Rook(1,0,'w','Rw')
        whitePawn = Pawn(2,1,'w','Pw')
        whiteBishop = Bishop(2,3,'w','Bw')

        self.whitePieces = {
            'Kw': whiteKing,
            'Rw': whiteRook,
            'Pw': whitePawn,
            'Bw': whiteBishop
        }

        # Black pieces
        blackKing = King(0, 0, 'b', 'Kb')

        self.blackPieces = {
            'Kb': blackKing
        }
      
        
        # combined pieceSet
        self.pieces = {**self.whitePieces, **self.blackPieces}

        # Place white pieces on the board
        for piece, obj in self.whitePieces.items():
            row, col = obj.row, obj.col
            self.board[row][col].set(obj)

        # Place black pieces on the board
        for piece, obj in self.blackPieces.items():
            row, col = obj.row, obj.col
            self.board[row][col].set(obj)
            
        self.player = 0
        self.nonCaptureMoves = 0
        self.depth = 0
    
    def print(self):
        print('-----------------')
        for row in self.board:
            print(' | '.join(['  ' if cell.piece is None else cell.piece.id[0] + cell.piece.color for cell in row]))
            print('-----------------')
    #################
    def generate_legal_moves(self):
        legalMoves = {}
        selectMoves = {}
        if self.player == 0:
            for piece, obj in self.blackPieces.items():
                capCheck, moves = obj.getMoves(self)
                if capCheck == True:
                    selectMoves[piece] = moves
                else:
                    if moves:
                        legalMoves[piece] = moves
            if selectMoves:
                return selectMoves
            else:
                return legalMoves
                    

        else:
            for piece, obj in self.whitePieces.items():
                capCheck, moves = obj.getMoves(self)
                if capCheck == True:
                    selectMoves[piece] = moves
                else:
                    if moves:
                        legalMoves[piece] = moves
            if selectMoves:
                return selectMoves
            else:
                return legalMoves
                      
class MedChessboard:
    def __init__(self, size=4):
        self.size = size
        self.board = [[Cell() for _ in range(size)] for _ in range(size)]
        self.whiteScore = 0
        self.blackScore = 0
        self.blackCheck = False
        self.whiteCheck = False

        # White pieces
        whiteKing = King(3, 0, 'w', 'Kw')
        whiteQueen = Queen(3,1, 'w', 'Qw')

        self.whitePieces = {
            'Kw': whiteKing,
            'Qw': whiteQueen
        }

        # Black pieces
        blackKing = King(0, 3, 'b', 'Kb')
        blackQueen = Queen(0,2, 'b', 'Qb')
        blackKnight1 = Knight (2, 3, 'b', 'N1b')
        blackKnight2 = Knight (2, 0, 'b', 'N2b')
        blackBishop = Bishop (0, 1, 'b', 'Bb')

        self.blackPieces = {
            'Kb': blackKing,
            'Qb': blackQueen,
            'N1b': blackKnight1,
            'N2b': blackKnight2,
            'Bb': blackBishop        }
      
        
        # combined pieceSet
        self.pieces = {**self.whitePieces, **self.blackPieces}

        # Place white pieces on the board
        for piece, obj in self.whitePieces.items():
            row, col = obj.row, obj.col
            self.board[row][col].set(obj)

        # Place black pieces on the board
        for piece, obj in self.blackPieces.items():
            row, col = obj.row, obj.col
            self.board[row][col].set(obj)
            
        self.player = 0
        self.nonCaptureMoves = 0
        self.depth = 0
    
    def print(self):
        print('-----------------')
        for row in self.board:
            print(' | '.join(['  ' if cell.piece is None else cell.piece.id[0] + cell.piece.color for cell in row]))
            print('-----------------')
    #################
    def generate_legal_moves(self):
        legalMoves = {}
        selectMoves = {}
        if self.player == 0:
            for piece, obj in self.blackPieces.items():
                capCheck, moves = obj.getMoves(self)
                if capCheck == True:
                    selectMoves[piece] = moves
                else:
                    if moves:
                        legalMoves[piece] = moves
            if selectMoves:
                return selectMoves
            else:
                return legalMoves
                    

        else:
            for piece, obj in self.whitePieces.items():
                capCheck, moves = obj.getMoves(self)
                if capCheck == True:
                    selectMoves[piece] = moves
                else:
                    if moves:
                        legalMoves[piece] = moves
            if selectMoves:
                return selectMoves
            else:
                return legalMoves
            
class HardChessboard1:
    def __init__(self, size=4):
        self.size = size
        self.board = [[Cell() for _ in range(size)] for _ in range(size)]
        self.whiteScore = 0
        self.blackScore = 0
        self.blackCheck = False
        self.whiteCheck = False

        # White pieces
        whiteKing = King(3, 0, 'w', 'Kw')
        whiteQueen = Queen(3, 1, 'w', 'Qw')
        whiteBishop = Bishop(3, 3, 'w', 'Bw')
        whiteKnight = Knight(2, 0, 'w', 'Nw')
        whitePawn = Pawn(2, 1, 'w', 'Pw')

        self.whitePieces = {
            'Kw': whiteKing,
            'Qw': whiteQueen,
            'Bw': whiteBishop,
            'Nw': whiteKnight,
            'Pw': whitePawn
        }

        # Black pieces
        blackKing = King(0, 0, 'b', 'Kb')
        blackQueen = Queen(1, 3, 'b', 'Qb')
        blackRook1 = Rook(0, 1, 'b', 'R1b')
        blackRook2 = Rook(0, 3, 'b', 'R2b')
        blackKnight1 = Knight(1, 0, 'b', 'N1b')
        blackKnight2 = Knight(0, 2, 'b', 'N2b')
        blackPawn = Pawn(1, 2, 'b', 'Pb')

        self.blackPieces = {
            'Kb': blackKing,
            'Qb': blackQueen,
            'R1b': blackRook1,
            'R2b': blackRook2,
            'N1b': blackKnight1,
            'N2b': blackKnight2,
            'Pb': blackPawn
        }
      
        
        # combined pieceSet
        self.pieces = {**self.whitePieces, **self.blackPieces}

        # Place white pieces on the board
        for piece, obj in self.whitePieces.items():
            row, col = obj.row, obj.col
            self.board[row][col].set(obj)

        # Place black pieces on the board
        for piece, obj in self.blackPieces.items():
            row, col = obj.row, obj.col
            self.board[row][col].set(obj)
            
        self.player = 0
        self.nonCaptureMoves = 0
        self.depth = 0
    
    def print(self):
        print('-----------------')
        for row in self.board:
            print(' | '.join(['  ' if cell.piece is None else cell.piece.id[0] + cell.piece.color for cell in row]))
            print('-----------------')
    #################
    def generate_legal_moves(self):
        legalMoves = {}
        selectMoves = {}
        if self.player == 0:
            for piece, obj in self.blackPieces.items():
                capCheck, moves = obj.getMoves(self)
                if capCheck == True:
                    selectMoves[piece] = moves
                else:
                    if moves:
                        legalMoves[piece] = moves
            if selectMoves:
                return selectMoves
            else:
                return legalMoves
                    

        else:
            for piece, obj in self.whitePieces.items():
                capCheck, moves = obj.getMoves(self)
                if capCheck == True:
                    selectMoves[piece] = moves
                else:
                    if moves:
                        legalMoves[piece] = moves
            if selectMoves:
                return selectMoves
            else:
                return legalMoves
                   
class HardChessboard2:
    def __init__(self, size=4):
        self.size = size
        self.board = [[Cell() for _ in range(size)] for _ in range(size)]
        self.whiteScore = 0
        self.blackScore = 0
        self.blackCheck = False
        self.whiteCheck = False

        # White pieces
        whiteKing = King(3, 0, 'w', 'Kw')
        whiteQueen = Queen(2, 3, 'w', 'Qw')
        whiteRook1 = Rook(3,1,'w','R1w')
        whiteKnight1 = Knight(3, 2, 'w', 'N1w')
        whiteKnight2 = Knight(2, 0, 'w', 'N2w')
        whitePawn = Pawn(2, 1, 'w', 'P1w')



        self.whitePieces = {
            'Kw': whiteKing,
            'Qw': whiteQueen,
            'R1w': whiteRook1,
            'N1w': whiteKnight1,
            'N2w': whiteKnight2,
            'P1w': whitePawn

        }

        # Black pieces
        blackKing = King(0, 0, 'b', 'Kb')
        blackQueen = Queen(0, 1, 'b', 'Qb')
        blackRook2 = Rook(1, 3, 'b', 'R2b')
        blackKnight1 = Knight(0, 2, 'b', 'N1b')
        blackPawn1 = Pawn(1, 0, 'b', 'P1b')
        blackPawn2 = Pawn(1, 1, 'b', 'P2b')


        self.blackPieces = {
            'Kb': blackKing,
            'Qb': blackQueen,
            'N1b': blackKnight1,
            'R2b': blackRook2,
            'P1b': blackPawn1,
            'P2b': blackPawn2


        }
      
        
        # combined pieceSet
        self.pieces = {**self.whitePieces, **self.blackPieces}

        # Place white pieces on the board
        for piece, obj in self.whitePieces.items():
            row, col = obj.row, obj.col
            self.board[row][col].set(obj)

        # Place black pieces on the board
        for piece, obj in self.blackPieces.items():
            row, col = obj.row, obj.col
            self.board[row][col].set(obj)
            
        self.player = 0
        self.nonCaptureMoves = 0
        self.depth = 0
    
    def print(self):
        print('-----------------')
        for row in self.board:
            print(' | '.join(['  ' if cell.piece is None else cell.piece.id[0] + cell.piece.color for cell in row]))
            print('-----------------')
    #################
    def generate_legal_moves(self):
        legalMoves = {}
        selectMoves = {}
        if self.player == 0:
            for piece, obj in self.blackPieces.items():
                capCheck, moves = obj.getMoves(self)
                if capCheck == True:
                    selectMoves[piece] = moves
                else:
                    if moves:
                        legalMoves[piece] = moves
            if selectMoves:
                return selectMoves
            else:
                return legalMoves
                    

        else:
            for piece, obj in self.whitePieces.items():
                capCheck, moves = obj.getMoves(self)
                if capCheck == True:
                    selectMoves[piece] = moves
                else:
                    if moves:
                        legalMoves[piece] = moves
            if selectMoves:
                return selectMoves
            else:
                return legalMoves


# Create a 4x4 chessboard with  (swap between versions above)
chessboard = None # placeholder

while True:
    choice = input("Select your starting configuration (1-5): ")
    if choice.isnumeric():
        choice = int(choice)
        if 1 <= choice <= 5:
            break
    print("Invalid input. Please enter an integer between 1 and 5.")
    print()

if choice == 1:
    print("You selected an easy configuration..")
    chessboard = EasyChessboard1()
elif choice == 2:
    print("You selected an easy configuration..")
    chessboard = EasyChessboard2()
elif choice == 3:
    print("You selected a medium configuration..")
    chessboard = MedChessboard()
elif choice == 4:
    print("You selected a hard configuration..")
    chessboard = HardChessboard1()
elif choice == 5:
    print("You selected a hard configuration..")
    chessboard = HardChessboard2()

                     
chessboard.print()  
  
utility, seq = backward_induction(chessboard,7)
del seq[-1]
if (utility != 0):
    print_sequence(seq)
gameOver(utility)






    

    
    
    