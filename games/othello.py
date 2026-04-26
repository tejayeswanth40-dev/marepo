import numpy as np
import pygame
from base import BaseGame

class othello(BaseGame):
    def __init__(self):
        self.board = np.zeros((8, 8), dtype=int)
        self.current_player = 1
        self.current_player_name = "Player 1"
        self.player_1_id = BaseGame.player1
        self.player_2_id = BaseGame.player2
        self.game_over = False
        self.screen = pygame.display.set_mode((600, 600))
        self.winner = None        
        self.blackcoins = 2
        self.whitecoins = 2
    
    def initial_board(self):
        board = np.zeros((8, 8), dtype=int)
        board[3 ,3] = 2
        board[3 ,4] = 1
        board[4 ,3] = 1
        board[4 ,4] = 2
        return board
    
    def draw_initial_screen(self):
        only_initial_board = self.initial_board()
        screen = pygame.display.set_mode((600, 600))
        screen.fill((0,128,0))

        for x in range(8):
            for y in range(8):
                rect = pygame.Rect(x*75, y*75, 75, 75)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)
                
                if only_initial_board[y, x] == 1:
                    pygame.draw.circle(screen, (0, 0, 0), rect.center, 30)
                elif only_initial_board[y, x] == 2:
                    pygame.draw.circle(screen, (255, 255, 255), rect.center, 30)

    def is_valid_move(self, board, r, c, player):
        if board[r, c] != 0:
            return False
        coin_position = (r, c)
        opponent = 3 - player
        coin_to_place = player
        other_coin = opponent
        row1 = board[r, :]   
        row1_position = r
        row2 = board[:, c].reshape(8,)
        row2_position = c
        diag1 = board.diagonal(c-r) 
        diag1
        diag2 = board[:,::-1].diagonal((7-c)-r)

        other_coin_found = False
        coin_found = False

        while not coin_found 





    def valid_moves(self, board, player):
        moves = []
        for x in range(8):
            for y in range(8):
                if self.is_valid_move(board, x, y, player):
                    moves.append((x, y))
        return moves
    

        
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
    def play(self):
        self.board = self.initial_board()
        self.draw_initial_screen()
        while