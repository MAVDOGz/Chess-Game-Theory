class Cell:
    def __init__(self, piece=None):
        self.piece = None
        self.color = None

    def set(self, piece):
        self.piece = piece
        self.color = piece.color

    def remove(self):
        self.piece = None
        self.color = None