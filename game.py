
import matplotlib.pyplot as plt
import pygame
import numpy as np
import sys
import subprocess
import csv
from datetime import datetime as dt
from base import BaseGame
from games import tictactoe
from games import connect4
from games import othello

pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game Hub")

title_font = pygame.font.SysFont("timesnewroman", 60, bold=True)
another_font = pygame.font.SysFont("timesnewroman", 40, italic=True)
button_font = pygame.font.SysFont("timesnewroman", 30)
small_font = pygame.font.SysFont("timesnewroman", 24)

icon_of_window = pygame.image.load("games/gamelogos/icon_of_window.jpg").convert()
icon_of_window = pygame.transform.scale(icon_of_window, (32, 32))
pygame.display.set_icon(icon_of_window)

bg_home = pygame.image.load("games/gamelogos/bg_homepage.jpg").convert()
bg_menu = pygame.image.load("games/gamelogos/bg_menupage.jpg").convert()
winner_bgpage = pygame.image.load("games/gamelogos/winner_bg.jpeg").convert()
    
bg_home = pygame.transform.smoothscale(bg_home, (W, H))
bg_menu = pygame.transform.smoothscale(bg_menu, (W, H))
winner_bgpage = pygame.transform.smoothscale(winner_bgpage, (W, H))

game1_img = pygame.image.load("games/gamelogos/tictactoe_icon.png").convert_alpha()
game2_img = pygame.image.load("games/gamelogos/othello_icon.png").convert_alpha()
game3_img = pygame.image.load("games/gamelogos/connect4_icon.png").convert_alpha()

game1_img = pygame.transform.smoothscale(game1_img, (150, 150))
game2_img = pygame.transform.smoothscale(game2_img, (150, 150))
game3_img = pygame.transform.smoothscale(game3_img, (150, 150))

HOME = 0
MENU = 1
GAME1_OVERVIEW = 2
GAME2_OVERVIEW = 3
GAME3_OVERVIEW = 4
GAME1_PLAYAGAIN = 5
GAME2_PLAYAGAIN = 6
GAME3_PLAYAGAIN = 7

current_screen = HOME

def append_results(game_cap, game):
    with open('history.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if (game_cap.winner == 1) | (game_cap.winner == "Player 1 Wins!"):
            writer.writerow([sys.argv[1],sys.argv[2],dt.now().strftime("%d-%m-%Y"),game])
        elif (game_cap.winner == 2) | (game_cap.winner == "Player 2 Wins!"):
            writer.writerow([sys.argv[2],sys.argv[1],dt.now().strftime("%d-%m-%Y"),game])

def draw_button(text, x, y, w, h):
    rect= pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, (200, 200, 200), rect)
    label= button_font.render(text, True, (0, 0, 0))
    screen.blit(label, (x + w // 2 - label.get_width() // 2, y + 10))
    return rect

def draw_another_button(text, x, y, w, h):
    rect= pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, (200, 200, 200), rect)
    button_title = small_font.render(text, True, (0, 0, 0))
    screen.blit(button_title, (x + w // 2 - button_title.get_width() // 2, y + 10))
    return rect

enter_btn = pygame.Rect(0,0,0,0)
game1_rect = pygame.Rect(0,0,0,0)
game2_rect = pygame.Rect(0,0,0,0)
game3_rect = pygame.Rect(0,0,0,0)

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
                    gameT = tictactoe.T3("Player 1", "Player 2")
                    pygame.draw.rect(screen, (255, 255, 0), game1_rect, 3)
                    gameT.play()
                    winnr = gameT.winner
                    append_results(gameT, "tictactoe")
                    current_screen = GAME1_OVERVIEW
                elif game2_rect.collidepoint(mx, my):
                    gameO = othello.O2("Player 1", "Player 2")
                    pygame.draw.rect(screen, (255, 255, 0), game2_rect, 3)
                    gameO.play()
                    winnr = gameO.winner
                    append_results(gameO, "othello")
                    current_screen = GAME2_OVERVIEW
                elif game3_rect.collidepoint(mx, my):
                    gameC = connect4.C4("Player 1", "Player 2")
                    pygame.draw.rect(screen, (255, 255, 0), game3_rect, 3)
                    gameC.play()
                    winnr = gameC.winner
                    append_results(gameC, "connect4")
                    current_screen = GAME3_OVERVIEW
            elif current_screen in [GAME1_OVERVIEW, GAME2_OVERVIEW, GAME3_OVERVIEW]:
                if sort_by_wins_btn.collidepoint(mx, my):
                    subprocess.run(["bash", "leaderboard.sh", "wins"])
                    subprocess.Popen(["python3", "show_plots.py"])
                elif sort_by_losses_btn.collidepoint(mx, my):
                    subprocess.run(["bash", "leaderboard.sh", "losses"])
                    subprocess.Popen(["python3", "show_plots.py"])
                elif sort_by_ratio_btn.collidepoint(mx, my):
                    subprocess.run(["bash", "leaderboard.sh", "win/loss_ratio"])
                    subprocess.Popen(["python3", "show_plots.py"])
                elif playagain_btn.collidepoint(mx, my):
                    current_screen = MENU
                elif exit_btn.collidepoint(mx, my):
                    pygame.quit()
                    sys.exit()

    if current_screen == HOME:
        
        screen.blit(bg_home, (0, 0))
        title = title_font.render("Game Hub", True, (255, 255, 255))
        screen.blit(title, (W//2 - title.get_width()//2, 100))
        enter_btn = draw_button("Enter into Hub", W//2 - 95, 300, 200, 50)
        if enter_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), enter_btn, 3)

    elif current_screen == MENU:
        
        screen.blit(bg_menu, (0, 0))
        title = title_font.render("Play your Games", True, (255, 255, 255))
        screen.blit(title, (W//2 - title.get_width()//2, 70))
        game1_rect = screen.blit(game1_img, (130, 250))
        game2_rect = screen.blit(game2_img, (325, 250))
        game3_rect = screen.blit(game3_img, (530, 250))
        screen.blit(small_font.render("Tic Tac Toe", True, (255,255,255)), (146, 430))
        screen.blit(small_font.render("Othello", True, (255,255,255)), (365, 430))
        screen.blit(small_font.render("Connect 4", True, (255,255,255)), (560, 430))
        if game1_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (25, 25, 20), game1_rect, 3)
        elif game2_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (25, 25, 20), game2_rect, 3)
        elif game3_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (25, 25, 20), game3_rect, 3)

    elif current_screen == GAME1_OVERVIEW:
        screen.blit(winner_bgpage, (0, 0))
        if winnr == 1:
            result_text = "Player 1 Wins!"
        elif winnr == 2:
            result_text = "Player 2 Wins!"
        else:
            result_text = "It's a Draw!"
        result_label = title_font.render(result_text, True, (255, 255, 255))
        
        screen.blit(result_label, (W//2 - result_label.get_width()//2, 80))
        statistics_title = another_font.render("View statistics", True, (255, 255, 255))
        screen.blit(statistics_title, (W//2 - statistics_title.get_width()//2, 180))
    
        sort_by_wins_btn = draw_button("Sort by Wins", W//2 - 100, 250, 200, 50)
        sort_by_losses_btn = draw_button("Sort by Losses", W//2 - 100, 310, 200, 50)
        sort_by_ratio_btn = draw_another_button("Sort by Win/Loss Ratio", W//2 - 125, 370, 250, 50)
        playagain_btn = draw_button("Return to menu", W//2 - 140, 450, 280, 55)
        exit_btn = draw_button("Exit", W//2 - 140, 520, 280, 55)

        if sort_by_wins_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), sort_by_wins_btn, 3)
        if sort_by_losses_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), sort_by_losses_btn, 3)
        if sort_by_ratio_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), sort_by_ratio_btn, 3)
        if playagain_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), playagain_btn, 3)
        if exit_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), exit_btn, 3)   

    elif current_screen == GAME2_OVERVIEW:
        screen.blit(winner_bgpage, (0, 0))
        if winnr == 1:
            result_text = "Player 1 Wins!"
        elif winnr == 2:
            result_text = "Player 2 Wins!"
        else:
            result_text = "It's a Draw!"
        result_label = title_font.render(result_text, True, (255, 255, 255))
        
        screen.blit(result_label, (W//2 - result_label.get_width()//2, 80))
        statistics_title = another_font.render("View statistics", True, (255, 255, 255))
        screen.blit(statistics_title, (W//2 - statistics_title.get_width()//2, 180))
        sort_by_wins_btn = draw_button("Sort by Wins", W//2 - 100, 250, 200, 50)
        sort_by_losses_btn = draw_button("Sort by Losses", W//2 - 100, 310, 200, 50)
        sort_by_ratio_btn = draw_another_button("Sort by Win/Loss Ratio", W//2 - 125, 370, 250, 50)
        playagain_btn = draw_button("Return to menu", W//2 - 140, 450, 280, 55)
        exit_btn = draw_button("Exit", W//2 - 140, 520, 280, 55)

        if sort_by_wins_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), sort_by_wins_btn, 3)
        if sort_by_losses_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), sort_by_losses_btn, 3)
        if sort_by_ratio_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), sort_by_ratio_btn, 3)
        if playagain_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), playagain_btn, 3)
        if exit_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), exit_btn, 3)   



    
    elif current_screen == GAME3_OVERVIEW:
        screen.blit(winner_bgpage, (0, 0))
        if winnr == 1:
            result_text = "Player 1 Wins!"
        elif winnr == 2:
            result_text = "Player 2 Wins!"
        else:
            result_text = "It's a Draw!"
        result_label = title_font.render(result_text, True, (255, 255, 255))
        
        screen.blit(result_label, (W//2 - result_label.get_width()//2, 80))
        statistics_title = another_font.render("View statistics", True, (255, 255, 255))
        screen.blit(statistics_title, (W//2 - statistics_title.get_width()//2, 180))
        sort_by_wins_btn = draw_button("Sort by Wins", W//2 - 100, 250, 200, 50)
        sort_by_losses_btn = draw_button("Sort by Losses", W//2 - 100, 310, 200, 50)
        sort_by_ratio_btn = draw_another_button("Sort by Win/Loss Ratio", W//2 - 125, 370, 250, 50)
        playagain_btn = draw_button("Return to menu", W//2 - 140, 450, 280, 55)
        exit_btn = draw_button("Exit", W//2 - 140, 520, 280, 55)

        if sort_by_wins_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), sort_by_wins_btn, 3)
        if sort_by_losses_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), sort_by_losses_btn, 3)
        if sort_by_ratio_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), sort_by_ratio_btn, 3)
        if playagain_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), playagain_btn, 3)
        if exit_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (0, 0, 0), exit_btn, 3)   


    pygame.display.update()

    
