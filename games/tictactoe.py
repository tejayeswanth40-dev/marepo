from base import BaseGame
import numpy as np
import pygame

class T3(BaseGame):
    def __init__(self, usrname1, usrname2):
        super().__init__(usrname1, usrname2, T3)
        self.side_length = 50
    # W1 is width of the leftmost vertical line from the left edge of the window
        self.W1 = (800 - 10 * self.side_length) // 2
    # H1 is height of the topmost horizontal line from the top edge of the window
        self.H1 = (800 - 10 * self.side_length) // 2
        self.winner = None
    def initialize_board(self):
        pygame.display.set_caption("Tic Tac Toe")
        self.screen1 = pygame.display.set_mode((800, 800))
    #Draw the grid lines for the 10x10 board
        for x in range(10):
            for y in range(10):
                rect = pygame.Rect(x * self.side_length + self.W1, y * self.side_length + self.H1, self.side_length, self.side_length)
                pygame.draw.rect(self.screen1, (0, 0, 0), rect, 1)

    @staticmethod
    def generate_board():
        return np.zeros((10,10), dtype=int)

    def if_valid_then_update(self, row, col, turn):
        if row < 0 or row >= 10 or col < 0 or col >= 10 or self.board[row, col] != 0:
            return False
        else:
            self.board[row, col] = turn
            self.switch_turn()
            return True
    def check_win(self):
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
        #diagonal(9-y-x) gives the diag wherever y+x is constant, it is diagonal(offset, axis1, axis2)
        diag2 = ''.join(map(str, self.board[:,::-1].diagonal(9-y-x)))
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

    # Draws coins placed and the grid lines
    def draw_board(self):
        for x in range(10):
            for y in range(10):
                rect = pygame.Rect(x * self.side_length + self.W1, y * self.side_length + self.H1, self.side_length, self.side_length)
                pygame.draw.rect(self.screen1, (0, 0, 0), rect, 1)
                if self.board[x, y] == 1:
                    self.draw_x(self.screen1, (255, 0, 0), rect.centerx , rect.centery, 30, 5)
                elif self.board[x, y] == 2:
                    pygame.draw.circle(self.screen1, (0, 0, 0), rect.center, 18, 5)
                    
    def play(self):
        pygame.init()
        self.initialize_board()
        title_font = pygame.font.SysFont("timesnewroman", 48, bold=True)
        game1_rect = pygame.Rect(0,0,800,800)
        T3_img = pygame.image.load('games/gamelogos/T3_background.jpg').convert_alpha()
        T3_img = pygame.transform.smoothscale(T3_img, (800, 800))
        clock = pygame.time.Clock()
        clock.tick(60)
        while True:

            # DESIGN VARIABLES START
            game1_rect = self.screen1.blit(T3_img, (0, 0))
            title = title_font.render(f"Player {self.current_turn}'s Turn", True, (0, 0, 0))
            title1 = title_font.render(": Player 1", True, (0, 0, 0))
            title2 = title_font.render(": Player 2", True, (0, 0, 0))
            self.screen1.blit(title, (250, 50))
            board_rect = pygame.Rect(self.W1, self.H1, 10 * self.side_length, 10 * self.side_length)
            board_rect1 = pygame.Rect(self.W1 + 5.5*self.side_length, self.H1 + 9.5* self.side_length + 50, self.side_length, self.side_length)
            board_rect2 = pygame.Rect(self.W1 - 0.5*self.side_length, self.H1 + 9.5* self.side_length + 50, self.side_length, self.side_length)
            # DESIGN VARIABLES END

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
                
                # DESIGN ELEMENTS TO BE UPDATED EVERY FRAME
            self.screen1.fill((255, 253, 235 ), board_rect1)
            self.screen1.fill((255, 253, 235 ), board_rect2)
            self.draw_x(self.screen1, (255, 0, 0), board_rect2.centerx , board_rect2.centery, 30, 5)
            pygame.draw.circle(self.screen1, (0, 0, 0), (self.W1 + 6*self.side_length, self.H1 + 10*self.side_length + 50), 18, 5)
            self.screen1.blit(title1, (self.W1 + 0*self.side_length + 30, self.H1 + 10*self.side_length + 22)) 
            self.screen1.blit(title2, (self.W1 + 6*self.side_length + 30, self.H1 + 10*self.side_length + 22))
            self.screen1.fill((255, 253, 235 ), board_rect)
            self.draw_board()
            pygame.display.update()
