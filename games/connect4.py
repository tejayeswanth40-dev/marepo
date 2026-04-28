from base import BaseGame
import numpy as np
import pygame

class C4(BaseGame):
    def __init__(self, usrname1, usrname2):
        super().__init__(usrname1, usrname2, C4)
        self.W3 = 20
        self.H3 = 60
        self.side_length = 80
        self.winner = None
    def initialize_board(self):
        pygame.display.set_caption("Connect 4")
        self.screen3 = pygame.display.set_mode((600, 600))
        for x in range(7):
            for y in range(6):
                rect = pygame.Rect(x * self.side_length + self.W3, y * self.side_length + self.H3, self.side_length, self.side_length)
                pygame.draw.rect(self.screen3, (0, 0, 0), rect, 1)
    
    @staticmethod
    def generate_board():
        return np.zeros((6,7), dtype=int)
    def if_valid_then_update(self, col, turn):
        if self.board[0, col] != 0:
            return False
        else:
            for row in range(5, -1, -1):
                if self.board[row, col] == 0:
                    self.board[row, col] = turn
                    self.switch_turn()
                    return True
    
    def check_win(self,col):
        if np.all(self.board[0,:] == 1):
            return 1
        elif np.all(self.board[0,:] == 2):
            return 2
        x,y = self.last_pos
        #FOR ROWS
        row = ''.join(map(str, self.board[x,:]))
        if '1111' in row:
            return 1
        elif '2222' in row:
            return 2
        #FOR COLUMNS
        col = ''.join(map(str, self.board[:,y]))
        if '1111' in col:
            return 1
        elif '2222' in col:
            return 2
        #FOR DIAGONALS
        #diagonal(y-x) gives the diag wherever y-x is constant, it is diagonal(offset, axis1, axis2)
        diag1 = ''.join(map(str, self.board.diagonal(y-x)))
        if len(diag1) >=4:
            if '1111' in diag1:
                return 1
            elif '2222' in diag1:
                return 2
        #diagonal(y+x) gives the diag wherever y+x is constant, it is diagonal(offset, axis1, axis2)
        diag2 = ''.join(map(str, self.board[:,::-1].diagonal(y+x)))
        if len(diag2) >=4:
            if '1111' in diag2:
                return 1
            elif '2222' in diag2:
                return 2
        return 0
    def draw_board(self):
        rect = pygame.Rect(self.W3, self.H3, 7 * self.side_length, 6* self.side_length)
        pygame.draw.rect(self.screen3, (0, 0, 0), rect, 1)
        for x in range(7):
            for y in range(6):
                circl = pygame.draw.circle(self.screen3, (0, 0, 128) , (x * self.side_length + self.W3 + self.side_length//2, y * self.side_length + self.H3 + self.side_length//2), 3/4 * self.side_length//2)
                if self.board[y, x] == 1:
                    pygame.draw.circle(self.screen3, (255, 255, 0), circl.center, 3/8 * self.side_length)
                elif self.board[y, x] == 2:
                    pygame.draw.circle(self.screen3 , (255, 0, 0), circl.center, 3/8 * self.side_length)
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
                    c = (mx - self.W3) // self.side_length
                    if self.if_valid_then_update(c, self.current_turn):
                        count = np.sum((self.board[:,c] == 1) | (self.board[:,c] == 2))
                        #since if_valid_then_update updates the board, count gives the number of pieces in that column after placing the piece, so the row_index of the piece placed is 6 - count.
                        r = 6 - count
                        self.last_pos = (r, c)
                        winner = self.check_win(c)
                        if winner:
                            self.winner = winner
                            print(f"Player {winner} wins!")
                            pygame.display.set_caption("Game Hub")
                            screen3=pygame.display.set_mode((800, 600))
                            return
            self.screen3.fill((135 , 206 , 235 ))
            self.draw_board()
            pygame.display.update()