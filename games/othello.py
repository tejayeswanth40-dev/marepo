import numpy as np
import pygame
from base import BaseGame

class O2(BaseGame):
    def __init__(self, usrname1, usrname2):
        super().__init__(usrname1, usrname2, O2)
        self.board = np.zeros((8, 8), dtype=int)
        self.current_player = 1
        self.current_player_name = "Player 1"
        self.player_1_id = self.player1
        self.player_2_id = self.player2
        self.game_over = False
        self.screen = pygame.display.set_mode((600, 600))
        self.winner = None        
        self.blackcoins = 2
        self.whitecoins = 2
        self.screen1 = None

    @staticmethod
    def generate_board():
        board = np.zeros((8, 8), dtype=int)
        board[3 ,3] = 2
        board[3 ,4] = 1
        board[4 ,3] = 1
        board[4 ,4] = 2
        return board
    
    def draw_initial_screen(self):
        only_initial_board = self.generate_board()
        self.screen1 = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Othello")
        self.screen1.fill((0,140,10))
       
        for x in range(8):
            for y in range(8):
                rect = pygame.Rect(x*75, y*75, 75, 75)
                pygame.draw.rect(self.screen1, (0, 0, 0), rect, 2)
                
                if only_initial_board[y, x] == 1:
                    pygame.draw.circle(self.screen1, (0, 0, 0), rect.center, 30)
                    pygame.draw.circle(self.screen1, (255, 255, 255), rect.center, 30, 1)
                elif only_initial_board[y, x] == 2:
                    pygame.draw.circle(self.screen1, (255, 255, 255), rect.center, 30)
                    pygame.draw.circle(self.screen1, (0, 0, 0), rect.center, 30, 1)

    def is_valid_move(self, board, r, c, player):

        if board[r, c] != 0:
            return 'f'
        
        coin_position = (r, c)
        opponent = 3 - player
        coin_to_place = player
        other_coin = opponent

        row1 = board[r, :]   
        row1_position = c
        row2 = board[:, c]
        row2_position = r
        diag1 = board.diagonal(c-r) 
    
        if c-r >= 0:
            diag1_position = r
            idiag1_position = r        
        else:
            diag1_position = c
            idiag1_position = c

        diag2 = board[:,::-1].diagonal((7-c)-r)
        if (7-c)-r >= 0:
            diag2_position = r 
            idiag2_position = r 
        else:
            diag2_position = (7-c)
            idiag2_position = (7-c)

        possible_directions = []
        row1_position +=1
        # Check rightside in rows
        while row1_position >= 0 and row1_position < 8 and row1[row1_position] != 0:
            if row1_position < 7 and row1[row1_position] == other_coin:
                row1_position += 1
                continue
            if row1_position != c + 1 and row1[row1_position] == coin_to_place:
                possible_directions.append('rr')
                break
            break
            
        # Check leftside in rows
        row1_position = c - 1
        while row1_position >= 0 and row1_position < 8 and row1[row1_position] != 0:
            if row1_position > 0 and row1[row1_position] == other_coin:
                row1_position -= 1
                continue
            if row1_position != c - 1 and row1[row1_position] == coin_to_place:
                possible_directions.append('lr')
                break
            break
               
        # Check downwards in columns
        row2_position += 1
        while row2_position >= 0 and row2_position < 8 and row2[row2_position] != 0:
            if row2_position < 7 and row2[row2_position] == other_coin:
                row2_position += 1
                continue
            if row2_position != r + 1 and row2[row2_position] == coin_to_place:
                possible_directions.append('dc')
                break
            break
        
        # Check upwards in columns
        row2_position = r - 1
        while row2_position >= 0 and row2_position < 8 and row2[row2_position] != 0:
            if row2_position > 0 and row2[row2_position] == other_coin:
                row2_position -= 1
                continue
            if row2_position != r - 1 and row2[row2_position] == coin_to_place:
                possible_directions.append('uc')
                break
            break
        
        # Check downwards in diag1
        diag1_position += 1
        while diag1_position >= 0 and diag1_position < len(diag1) and diag1[diag1_position] != 0:
            if diag1_position < len(diag1) - 1 and diag1[diag1_position] == other_coin:
                diag1_position += 1
                continue
            if diag1_position != idiag1_position + 1 and diag1[diag1_position] == coin_to_place:
                possible_directions.append('dd1')
                break
            break
        
        # Check upwards in diag1
        diag1_position = idiag1_position - 1
        while diag1_position >= 0 and diag1_position < len(diag1) and diag1[diag1_position] != 0:
            if diag1_position > 0 and diag1[diag1_position] == other_coin:
                diag1_position -= 1
                continue
            if diag1_position != idiag1_position - 1 and diag1[diag1_position] == coin_to_place:
                possible_directions.append('ud1')
                break
            break
            
        # Check downwards in diag2
        diag2_position += 1
        while diag2_position >= 0 and diag2_position < len(diag2) and diag2[diag2_position] != 0:
            if diag2_position < len(diag2) - 1 and diag2[diag2_position] == other_coin:
                diag2_position += 1
                continue
            if diag2_position != idiag2_position + 1 and diag2[diag2_position] == coin_to_place:
                possible_directions.append('dd2')
                break
            break

        # Check upwards in diag2
        diag2_position = idiag2_position - 1
        while diag2_position >= 0 and diag2_position < len(diag2) and diag2[diag2_position] != 0:
            if diag2_position > 0 and diag2[diag2_position] == other_coin:
                diag2_position -= 1
                continue
            if diag2_position != idiag2_position - 1 and diag2[diag2_position] == coin_to_place:
                possible_directions.append('ud2')
                break
            break

        if possible_directions != []:
            return possible_directions    
        else:
            return 'f'
        

    def valid_moves(self, board, player):
        moves = []
        for x in range(8):
            for y in range(8):
                if self.is_valid_move(board, x, y, player) != 'f':
                    moves.append((x, y))
        return moves

    def updated_board_after_move(self, board, r, c, player):
        temp_board = np.copy(board)

        if self.is_valid_move(board, r, c, player) == 'f':
            return board
               
        if 'rr' in self.is_valid_move(board, r, c, player):
            c1 = c + 1
            while temp_board[r, c1] != player:
                temp_board[r, c1] = player
                c1 += 1
        if 'lr' in self.is_valid_move(board, r, c, player):
            c1 = c - 1
            while temp_board[r, c1] != player:
                temp_board[r, c1] = player
                c1 -= 1
        if 'dc' in self.is_valid_move(board, r, c, player):
            r1 = r + 1
            while temp_board[r1, c] != player:
                temp_board[r1, c] = player
                r1 += 1
        if 'uc' in self.is_valid_move(board, r, c, player):
            r1 = r - 1
            while temp_board[r1, c] != player:
                temp_board[r1, c] = player
                r1 -= 1
        if 'dd1' in self.is_valid_move(board, r, c, player):
            r1 = r + 1
            c1 = c + 1
            while temp_board[r1, c1] != player:
                temp_board[r1, c1] = player
                r1 += 1
                c1 += 1
        if 'ud1' in self.is_valid_move(board, r, c, player):
            r1 = r - 1
            c1 = c - 1
            while temp_board[r1, c1] != player:
                temp_board[r1, c1] = player
                r1 -= 1
                c1 -= 1
        if 'dd2' in self.is_valid_move(board, r, c, player):
            r1 = r + 1
            c1 = c - 1
            while temp_board[r1, c1] != player:
                temp_board[r1, c1] = player
                r1 += 1
                c1 -= 1
        if 'ud2' in self.is_valid_move(board, r, c, player):
            r1 = r - 1
            c1 = c + 1
            while temp_board[r1, c1] != player:
                temp_board[r1, c1] = player
                r1 -= 1
                c1 += 1

        temp_board[r, c] = player

        return temp_board

    def draw_screen_after_updated_board(self, board):    
        self.screen1.fill((0,140,10))
        for x in range(8):
            for y in range(8):
                rect = pygame.Rect(x*75, y*75, 75, 75)
                pygame.draw.rect(self.screen1, (0, 0, 0), rect, 2)
                
                if board[y, x] == 1:
                    pygame.draw.circle(self.screen1, (0, 0, 0), rect.center, 30)
                    pygame.draw.circle(self.screen1, (255, 255, 255), rect.center, 30, 1)
                elif board[y, x] == 2:
                    pygame.draw.circle(self.screen1, (255, 255, 255), rect.center, 30)
                    pygame.draw.circle(self.screen1, (0, 0, 0), rect.center, 30, 1)

    def draw_valid_moves_positions(self, board, player):
        possible_valid_moves = self.valid_moves(board, player)
        for r, c in possible_valid_moves:
            rect = pygame.Rect(c*75, r*75, 75, 75)
            pygame.draw.circle(self.screen1, (120, 0, 140), rect.center, 29 ,2)

    def black_count(self, board):
        return np.sum(board == 1)
    
    def white_count(self, board):
        return np.sum(board == 2)

    def check_the_winner(self, board):
        player1_count = self.black_count(board)
        player2_count = self.white_count(board)
        if player1_count > player2_count:
            return "Player 1 Wins!"
        elif player2_count > player1_count:
            return "Player 2 Wins!"
        else:
            return "It's a tie!"

    def end_game(self, board, player):
        if self.valid_moves(board, player) == [] and self.valid_moves(board, 3 - player) == []:
            return True
        return False
    
    def play(self):
        self.board = self.generate_board()
        
        pygame.init()
        self.screen1 = pygame.display.set_mode((600, 600))
        self.draw_initial_screen()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    r, c = my // 75, mx // 75
                    if self.valid_moves(self.board, self.current_player) != []:
                        if self.is_valid_move(self.board, r, c, self.current_player) != 'f':
                            self.board = self.updated_board_after_move(self.board, r, c, self.current_player)
                            self.blackcoins = self.black_count(self.board)
                            self.whitecoins = self.white_count(self.board)
                            if self.end_game(self.board, self.current_player):
                                self.game_over = True
                                self.winner = self.check_the_winner(self.board)
                                return
                            else:
                                self.current_player = 3 - self.current_player
                                if self.current_player == 1:
                                    self.current_player_name = "Player 1"
                                else:
                                    self.current_player_name = "Player 2"

                    elif self.valid_moves(self.board, self.current_player) == []:
                        self.current_player = 3 - self.current_player
                        if self.current_player == 1:
                            self.current_player_name = "Player 1"
                        else:
                            self.current_player_name = "Player 2"
                        if self.end_game(self.board, self.current_player):
                            self.game_over = True
                            self.winner = self.check_the_winner(self.board)
                            return
                        


            self.draw_screen_after_updated_board(self.board)
            self.draw_valid_moves_positions(self.board, self.current_player)
            pygame.display.update()