from game import BaseGame
import numpy as np

class T3(BaseGame):
    def __init__(self, usrname1, usrname2):
        super().__init__(usrname1, usrname2, T3)

    def generate_board(self):
        return np.zeros((10,10), dtype=int)

    def make_move(self, row, col, turn):
        if self.board[row, col] != 0:
            return False
        else:
            self.board[row, col] = turn
            return True
    def check_win(self):
        if np.all(self.board[0,:] == 1):
            return 1
        elif np.all(self.board[0,:] == 2):
            return 2
        