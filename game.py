import pygame
import numpy as np
import sys
import subprocess

class BaseGame:
    def __init__(self, usrname1, usrname2, gameclass):
        self.player1 = usrname1
        self.player2 = usrname2
        self.board = gameclass.generate_board()
        self.current_turn = 1
        self.game = gameclass
        self.winner = None

    def switch_turn(self):
        if self.current_turn == 1:
            self.current_turn = 2
        else:
            self.current_turn = 1

# Import game modules after BaseGame is defined to avoid circular imports
from games import tictactoe
from games import connect4
from games import othello

pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game Hub")

title_font = pygame.font.SysFont("timesnewroman", 60, bold=True)
button_font = pygame.font.SysFont("timesnewroman", 30)
small_font = pygame.font.SysFont("timesnewroman", 24)

icon_of_window = pygame.image.load("games/gamelogos/icon_of_window.jpg").convert()
icon_of_window = pygame.transform.scale(icon_of_window, (32, 32))
pygame.display.set_icon(icon_of_window)

bg_home = pygame.image.load("games/gamelogos/bg_homepage.jpg").convert()
bg_menu = pygame.image.load("games/gamelogos/bg_menupage.jpg").convert()

bg_home = pygame.transform.smoothscale(bg_home, (W, H))
bg_menu = pygame.transform.smoothscale(bg_menu, (W, H))

game1_img = pygame.image.load("games/gamelogos/tictactoe_icon.png").convert_alpha()
game2_img = pygame.image.load("games/gamelogos/othello_icon.png").convert_alpha()
game3_img = pygame.image.load("games/gamelogos/connect4_icon.png").convert_alpha()

game1_img = pygame.transform.smoothscale(game1_img, (150, 150))
game2_img = pygame.transform.smoothscale(game2_img, (150, 150))
game3_img = pygame.transform.smoothscale(game3_img, (150, 150))

HOME = 0
MENU = 1

current_screen = HOME

def draw_button(text, x, y, w, h):
    rect= pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, (200, 200, 200), rect)
    label= button_font.render(text, True, (0, 0, 0))
    screen.blit(label, (x + 10, y + 10))
    return rect

enter_btn = pygame.Rect(0,0,0,0)
game1_rect = pygame.Rect(0,0,0,0)
game2_rect = pygame.Rect(0,0,0,0)
game3_rect = pygame.Rect(0,0,0,0)
screen.fill((0, 0, 0))

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my =pygame.mouse.get_pos()
            if current_screen == HOME:
                if enter_btn.collidepoint(mx, my):
                    current_screen = MENU
            elif current_screen == MENU:
                if game1_rect.collidepoint(mx, my):
                    pygame.draw.rect(screen, (255, 255, 0), game1_rect, 3)
                    tictactoe.play()    
                elif game2_rect.collidepoint(mx, my):
                    pygame.draw.rect(screen, (255, 255, 0), game2_rect, 3)
                    othello.play()
                elif game3_rect.collidepoint(mx, my):
                    pygame.draw.rect(screen, (255, 255, 0), game3_rect, 3)
                    connect4.play()

    if current_screen == HOME:
        screen.blit(bg_home, (0, 0))
        title = title_font.render("Game Hub", True, (255, 255, 255))
        screen.blit(title, (W//2 - title.get_width()//2, 100))
        enter_btn = draw_button("Enter into Hub", W//2 - 95, 300, 200, 50)
        if enter_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 0), enter_btn, 3)

    elif current_screen == MENU:
        screen.blit(bg_menu, (0, 0))
        title = title_font.render("Play your Games", True, (255, 255, 255))
        screen.blit(title, (W//2 - title.get_width()//2, 70))
        game1_rect = screen.blit(game1_img, (130, 250))
        game2_rect = screen.blit(game2_img, (325, 250))
        game3_rect = screen.blit(game3_img, (530, 250))
        screen.blit(small_font.render("Tic Tac Toe", True, (255,255,255)), (146, 435))
        screen.blit(small_font.render("Othello", True, (255,255,255)), (365, 435))
        screen.blit(small_font.render("Connect 4", True, (255,255,255)), (560, 435))

    pygame.display.update()