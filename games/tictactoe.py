from game import BaseGame
import numpy as np
import pygame

class T3(BaseGame):
    def __init__(self, usrname1, usrname2):
        super().__init__(usrname1, usrname2, T3)

    def generate_board(self):
        return np.zeros((10,10), dtype=int)

    def if_valid_then_move(self, row, col, turn):
        if self.board[row, col] != 0:
            return False
        else:
            self.board[row, col] = turn
            self.switch_turn()
            return True
    def check_win(self):
        if np.all(self.board[0,:] == 1):
            return 1
        elif np.all(self.board[0,:] == 2):
            return 2
        x,y = self.last_pos
        #FOR ROWS
        row = ''.join(map(str, self.board[x,:]))
        if '11111' in row:
            return 1
        elif '22222' in row:
            return 2
        #FOR COLUMNS
        col = ''.join(map(str, self.board[:,y]))
        if '11111' in col:
            return 1
        elif '22222' in col:
            return 2
        #FOR DIAGONALS
        #diagonal(y-x) gives the diag wherever y-x is constant, it is diagonal(offset, axis1, axis2)
        diag1 = ''.join(map(str, self.board.diagonal(y-x)))
        if len(diag1) >=5:
            if '11111' in diag1:
                return 1
            elif '22222' in diag2:
                return 2
        #diagonal(y+x) gives the diag wherever y+x is constant, it is diagonal(offset, axis1, axis2)
        diag2 = ''.join(map(str, self.board[:,::-1].diagonal(y+x)))
        if len(diag2) >=5:
            if '11111' in diag2:
                return 1
            elif '22222' in diag2:
                return 2
        return 0