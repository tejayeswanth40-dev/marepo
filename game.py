import pygame
import sys
import subprocess

pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game Hub")
icon_of_window = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon_of_window)

bg_home = pygame.image.load("bg_home.jpg")
bg_menu = pygame.image.load("bg_menu.jpg")
bg_home = pygame.transform.scale(bg_home, (W, H))
bg_menu = pygame.transform.scale(bg_menu, (W, H))

game1_img = pygame.image.load("game1.jpg")
game2_img = pygame.image.load("game2.jpg")
game3_img = pygame.image.load("game3.jpg")
game1_img = pygame.transform.scale(game1_img, (150, 150))
game2_img = pygame.transform.scale(game2_img, (150, 150))
game3_img = pygame.transform.scale(game3_img, (150, 150))

title_font = pygame.font.SysFont("timesnewroman", 50, bold=True)
button_font = pygame.font.SysFont("timesnewroman", 30)
small_font = pygame.font.SysFont("timesnewroman", 24)

HOME = 0
MENU = 1
GAME1 = 2
GAME2 = 3
GAME3 = 4

current_screen = HOME

def draw_button(text, x, y, w, h):
    rect= pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, (200, 200, 200), rect)
    label= button_font.render(text, True, (0, 0, 0))
    screen.blit(label, (x + 10, y + 10))
    return rect

running = True
while running:
    screen.fill((0, 0, 0))

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
                    current_screen = GAME1
                elif game2_rect.collidepoint(mx, my):
                    current_screen = GAME2
                elif game3_rect.collidepoint(mx, my):
                    current_screen = GAME3

            elif current_screen in [GAME1, GAME2, GAME3]:
                if play_btn.collidepoint(mx, my):
                    if current_screen == GAME1:
                        subprocess.run(["python", "tictactoe.py"])
                    elif current_screen == GAME2:
                        subprocess.run(["python", "othello.py"])
                    elif current_screen == GAME3:
                        subprocess.run(["python", "connect4.py"])

    if current_screen == HOME:
        screen.blit(bg_home, (0, 0))
        title = title_font.render("Game Hub", True, (255, 255, 255))

    elif current_screen == MENU:
        screen.blit(bg_menu, (0, 0))
        title = title_font.render("Select a Game", True, (255, 255, 255))
        game1_rect = screen.blit(game1_img, (150, 150))
        game2_rect = screen.blit(game2_img, (325, 150))
        game3_rect = screen.blit(game3_img, (500, 150))
        screen.blit(small_font.render("A", True, (255,255,255)), (200, 310))
        screen.blit(small_font.render("B", True, (255,255,255)), (375, 310))
        screen.blit(small_font.render("C", True, (255,255,255)), (550, 310))

    elif current_screen in [GAME1, GAME2, GAME3]:
        screen.fill((50, 50, 50))
        title = title_font.render("Game Screen", True, (255, 255, 255))

    pygame.display.update()
