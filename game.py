import numpy as np

class BaseGame:
    def __init__(self, usrname1, usrname2, rows, cols, game_name):
        self.player1 = usrname1
        self.player2 = usrname2
        self.rows = rows
        self.cols = cols
        self.game = game_name 
        self.current_turn = 1
    
    def switch_turn(self):
        if self.current_turn == 1:
            self.current_turn = 2
        else:
            self.current_turn = 1
    