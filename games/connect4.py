from game import BaseGame
import numpy as np

class Connect4(BaseGame):
    def __init__(self, usrname1, usrname2):
        super().__init__(usrname1, usrname2, Connect4)
    
    def generate_board(self):
        return np.zeros((6,7), dtype=int)
    def make_move(self, col, turn):
        if self.board[0, col] != 0:
            return False
        else:
            for row in range(5, -1, -1):
                if self.board[row, col] == 0:
                    self.board[row, col] = turn
                    return True
