from base import BaseGame
import numpy as np
import pygame

#Connect4 gameclass that inherits from basegame class.
#Contains important methods and attributes for the functionality 
class C4(BaseGame):
    def __init__(self, usrname1, usrname2):
        super().__init__(usrname1, usrname2, C4)
        self.side_length = 80
        # W3 is width of the leftmost vertical line from the left edge of the window
        self.W3 = (800 - 7 * self.side_length) // 2
        # H3 is height of the topmost horizontal line from the top edge of the window
        self.H3 = (800 - 7 * self.side_length) // 2
        self.side_length = 80
        self.winner = None
    def initialize_board(self):
        pygame.display.set_caption("Connect 4")
        self.screen3 = pygame.display.set_mode((800, 800))
        #Draw the grid lines for the 7x7 board
        for x in range(7):
            for y in range(7):
                rect = pygame.Rect(x * self.side_length + self.W3, y * self.side_length + self.H3, self.side_length, self.side_length)
                pygame.draw.rect(self.screen3, (0, 0, 0), rect, 1)
    
    @staticmethod
    def generate_board():
        return np.zeros((7,7), dtype=int)

    def if_valid_then_update(self, col, turn):
        if col < 0 or col >= 7 or self.board[0, col] != 0:
            return False
        else:
            for row in range(6, -1, -1):
                if self.board[row, col] == 0:
                    self.board[row, col] = turn
                    BaseGame.switch_turn(self)
                    return True
    
    def check_win(self,col):
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
        #diagonal(6-y-x) gives the diag wherever y+x is constant, it is diagonal(offset, axis1, axis2)
        diag2 = ''.join(map(str, self.board[:,::-1].diagonal(6-y-x)))
        if len(diag2) >=4:
            if '1111' in diag2:
                return 1
            elif '2222' in diag2:
                return 2
        return 0

        #Draw coins placed and the grid lines
    def draw_board(self):
        rect = pygame.Rect(self.W3, self.H3, 7 * self.side_length, 7 * self.side_length)
        pygame.draw.rect(self.screen3, (135 , 206 , 235 ), rect, 1)
        for x in range(7):
            for y in range(7):
                circl = pygame.draw.circle(self.screen3, (0, 0, 128) , (x * self.side_length + self.W3 + self.side_length//2, y * self.side_length + self.H3 + self.side_length//2), 3/4 * self.side_length//2)
                if self.board[y, x] == 1:
                    pygame.draw.circle(self.screen3, (255, 255, 0), circl.center, 3/8 * self.side_length)
                elif self.board[y, x] == 2:
                    pygame.draw.circle(self.screen3 , (255, 0, 0), circl.center, 3/8 * self.side_length)

    #Main game loop that runs the game,graphics
    def play(self):
        pygame.init()
        self.initialize_board()
        # DESIGN VARIABLES START
        title_font = pygame.font.SysFont("timesnewroman", 48, bold=True)
        game3_rect = pygame.Rect(0,0,800,800)
        C4_img = pygame.image.load('games/gamelogos/C4_background.jpg').convert_alpha()
        C4_img = pygame.transform.smoothscale(C4_img, (800, 800))
        # DESIGN VARIABLES END
        clock = pygame.time.Clock()
        clock.tick(60)
        while True:

            # DESIGN ELEMENTS TO BE UPDATED EVERY FRAME
            self.screen3.blit(C4_img, (0, 0))
            title = title_font.render(f"Player {self.current_turn}'s Turn", True, (0, 0, 0))
            title1 = title_font.render(": Player 1", True, (0, 0, 0))
            title2 = title_font.render(": Player 2", True, (0, 0, 0))
            self.screen3.blit(title, (250, 50))
            self.screen3.blit(title1, (self.W3 + self.side_length - 10, self.H3 + 7 * self.side_length + 22))
            self.screen3.blit(title2, (self.W3 + 4 * self.side_length + 35, self.H3 + 7 * self.side_length + 22))
            pygame.draw.circle(self.screen3, (255, 255, 0) , (0.5*self.side_length + self.W3, 7.5* self.side_length + self.H3 + 5 ), 3/4 * self.side_length//2)
            pygame.draw.circle(self.screen3, (255, 0, 0) , (4*self.side_length + self.W3, 7.5* self.side_length + self.H3 + 5 ), 3/4 * self.side_length//2)
            rect = pygame.Rect(self.W3, self.H3, 7 * self.side_length, 7 * self.side_length)

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
                        r = 7 - count
                        self.last_pos = (r, c)
                        winner = self.check_win(c)
                        if winner:
                            self.winner = winner
                            print(f"Player {winner} wins!")
                            pygame.display.set_caption("Game Hub")
                            screen3=pygame.display.set_mode((800, 600))
                            return
            self.screen3.fill((135 , 206 , 235 ),rect) # Sky blue background
            self.draw_board()
            pygame.display.update()