import numpy as np
import tictactoe.py as t3
import connect4.py as c4

class BaseGame:
    def __init__(self, usrname1, usrname2, gameclass):
        self.player1 = usrname1
        self.player2 = usrname2
        self.board = gameclass.generate_board()
        self.current_turn = 1
        self.game = gameclass
        self.winner = 0

    def switch_turn(self):
        if self.current_turn == 1:
            self.current_turn = 2
        else:
            self.current_turn = 1
    