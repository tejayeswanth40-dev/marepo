class BaseGame:
    def __init__(self, usrname1, usrname2, gameclass):
        self.player1 = usrname1
        self.player2 = usrname2
        self.board = gameclass.generate_board()
        self.current_turn = 1
        self.game = gameclass
        self.winner = None

        def switch_turn(self):
            self.current_turn = 3 - self.current_turn