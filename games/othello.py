import numpy as np
import pygame
class Othello(BaseGame):
    def __init__(self):
        self.board = np.zeros((8, 8), dtype=int)
        self.board[3][3] = 2
        self.board[3][4] = 1
        self.board[4][3] = 1
        self.board[4][4] = 2
        self.current_player = 1
        self.current_player_name = "Player 1"
        self.player_1_id = BaseGame.PLAYER1_id
        self.player_2_id = BaseGame.PLAYER2_id
        self.game_over = False
        self.winner = None
        self.screen = pygame.display.set_mode((400, 400))
        self.blackcoins = 2
        self.whitecoins = 2
    def draw_board(self, board):
    for x in range(8):
        for y in range(8):
            rect = pygame.Rect(x * 50, y * 50, 50, 50)
            pygame.draw.rect(self.screen, (0, 128, 0), rect)
            if board[y][x] == 1:
                pygame.draw.circle(self.screen, (0, 0, 0), rect.center, 20)
            elif board[y][x] == 2:
                pygame.draw.circle(self.screen, (255, 255, 255), rect.center, 20)

    def is_valid_move(self, board, x, y, player):
    if board[y][x] != 0:
        return False
    opponent = 3 - player
    coin_to_place = player
    other_coin = opponent
    

        

    def valid_moves(self, board, player):
        moves = []
        for x in range(8):
            for y in range(8):
                if board[y][x] == 0 and self.is_valid_move(board, x, y, player):
                    moves.append((x, y))
        return moves

    def update_board(self, board, x, y, player):
        
    def make_move(self, board, player):
    moves = self.valid_moves(board, player)
    if moves:
        x, y = moves[0]
        self.update_board(board, x, y, player)

    def check_the_winner(self, board):
        player1_count = np.sum(board == 1)
        player2_count = np.sum(board == 2)
        if player1_count > player2_count:
            return "Player 1 wins!"
        elif player2_count > player1_count:
            return "Player 2 wins!"
        else:
            return "It's a tie!"

    def end_game(self, board, player):
        if self.valid_moves(board, player) == [] and self.valid_moves(board, 3 - player) == []:
            return True
        return False

othello = Othello()

while not othello.game_over:
    