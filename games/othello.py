import numpy as np
import pygame
class Othello(BaseGame):
    def __init__(self):
        self.board = np.zeros((8, 8), dtype=int)
        self.current_player = 1
        self.game_over = False

    def draw_board(board):
    for x in range(8):
        for y in range(8):
            rect = pygame.Rect(x * 50, y * 50, 50, 50)
            pygame.draw.rect(screen, (0, 128, 0), rect)
            if board[y][x] == 1:
                pygame.draw.circle(screen, (255, 255, 255), rect.center, 20)
            elif board[y][x] == 2:
                pygame.draw.circle(screen, (0, 0, 0), rect.center, 20)

    def is_valid_move(board, x, y, player):
    if board[y][x] != 0:
        return False
        else:
            opponent = 3 - player
            movements = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dx, dy in movements:
                next_x = x + dx
                next_y = y + dy
                found_opponent = False
                while 0 <= next_x < 8 and 0 <= next_y < 8:
                    if board[next_y][next_x] == opponent:
                        found_opponent = True
                    elif board[next_y][next_x] == player and found_opponent:
                        return True
                    else:
                        break
                    next_x = next_x + dx
                    next_y = next_y + dy
        

    def valid_moves(board, player):
        moves = []
        for x in range(8):
            for y in range(8):
                if board[y][x] == 0 and self.is_valid_move(board, x, y, player):
                    moves.append((x, y))
        return moves

    def update_board(board, x, y, player):
        board[y][x] = player
        opponent = 3 - player
        movements = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dx, dy in movements:
            next_x = x + dx
            next_y = y + dy
            to_flip = []
            while 0 <= next_x < 8 and 0 <= next_y < 8:
                if board[next_y][next_x] == opponent:
                to_flip.append((next_x, next_y))
                elif board[next_y][next_x] == player:
                    for fx, fy in to_flip:
                    board[fy][fx] = player
                    break
                else:
                    break
            next_x = next_x + dx
            next_y = next_y + dy

    def make_move(board, player):
    moves = self.valid_moves(board, player)
    if moves:
        x, y = moves[0]
        self.update_board(board, x, y, player)

    def check_the_winner(board):
        player1_count = np.sum(board == 1)
        player2_count = np.sum(board == 2)
        if player1_count > player2_count:
            return "Player 1 wins!"
        elif player2_count > player1_count:
            return "Player 2 wins!"
        else:
            return "It's a tie!"

    def end_game(board, player):
        if self.valid_moves(board, player) == [] and self.valid_moves(board, 3 - player) == []:
            return True
        return False
