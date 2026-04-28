from base import BaseGame
import numpy as np
import pygame

class T3(BaseGame):
    def __init__(self, usrname1, usrname2):
        super().__init__(usrname1, usrname2, T3)
        self.W1 = 200
        self.H1 = 200
        self.side_length = 40
        self.winner = None
    def initialize_board(self):
        pygame.display.set_caption("Tic Tac Toe")
        self.screen1 = pygame.display.set_mode((800, 800))
        for x in range(10):
            for y in range(10):
                rect = pygame.Rect(x * self.side_length + self.W1, y * self.side_length + self.H1, self.side_length, self.side_length)
                pygame.draw.rect(self.screen1, (0, 0, 0), rect, 1)

    @staticmethod
    def generate_board():
        return np.zeros((10,10), dtype=int)

    def if_valid_then_update(self, row, col, turn):
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
            elif '22222' in diag1:
                return 2
        #diagonal(y+x) gives the diag wherever y+x is constant, it is diagonal(offset, axis1, axis2)
        diag2 = ''.join(map(str, self.board[:,::-1].diagonal(y+x)))
        if len(diag2) >=5:
            if '11111' in diag2:
                return 1
            elif '22222' in diag2:
                return 2
        return 0
    def draw_x(self, surface, color, center_x, center_y, size, thickness):
    #Draws an X-shaped cross centered at (center_x, center_y)

    # Top-left to bottom-right line
        pygame.draw.line(surface, color, 
                     (center_x - size//2, center_y - size//2), 
                     (center_x + size//2, center_y + size//2), thickness)
    
    # Top-right to bottom-left line
        pygame.draw.line(surface, color, 
                     (center_x + size//2, center_y - size//2), 
                     (center_x - size//2, center_y + size//2), thickness)

    def draw_board(self):
        for x in range(10):
            for y in range(10):
                rect = pygame.Rect(x * self.side_length + self.W1, y * self.side_length + self.H1, self.side_length, self.side_length)
                pygame.draw.rect(self.screen1, (0, 0, 0), rect, 1)
                if self.board[x, y] == 1:
                    self.draw_x(self.screen1, (0, 0, 0), rect.centerx , rect.centery, 30, 5)
                elif self.board[x, y] == 2:
                    pygame.draw.circle(self.screen1, (255, 0, 0), rect.center, 15, 5)
    def play(self):
        pygame.init()
        self.initialize_board()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    col, row = (my - self.H1) // self.side_length, (mx - self.W1) // self.side_length
                    if self.if_valid_then_update(row, col, self.current_turn):
                        self.last_pos = (row, col)
                        winner = self.check_win()
                        if winner:
                            self.winner = winner
                            print(f"Player {winner} wins!")
                            pygame.display.set_caption("Game Hub")
                            screen1=pygame.display.set_mode((800, 600))
                            return
            self.screen1.fill((255 , 255 , 255 ))
            self.draw_board()
            pygame.display.update()
