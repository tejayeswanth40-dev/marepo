from game import BaseGame
import numpy as np

class T3(BaseGame):
    def __init__(self, usrname1, usrname2):
        super().__init__(usrname1, usrname2, 10, 10, "Tic Tac Toe")
        #not over yet
        #BOARD IS NOT YET DEFINED WILL DEFINE LATER AS PER THE REQUIREMENTS
    def check_win(self):
        if np.all(self.board[0,:] == 1):
            return 1
        elif np.all(self.board[0,:] == 2):
            return 2
        