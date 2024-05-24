import numpy as np
import random
import pygame
import sys
import math

class Config:
    def __init__(self, row_count=6, column_count=7, player_piece=1, ai_piece=2, window_length=4):
        self.ROW_COUNT = row_count
        self.COLUMN_COUNT = column_count
        self.PLAYER_PIECE = player_piece
        self.AI_PIECE = ai_piece
        self.WINDOW_LENGTH = window_length

class Connect4Game:
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    def __init__(self, config=Config(), starting_player="player"):
        self.config = config
        self.board = self.create_board()
        self.SQUARESIZE = 100
        self.width = self.config.COLUMN_COUNT * self.SQUARESIZE
        self.height = (self.config.ROW_COUNT + 1) * self.SQUARESIZE
        self.size = (self.width, self.height)
        self.RADIUS = int(self.SQUARESIZE / 2 - 5)
        self.screen = None
        self.myfont = None
        self.game_over = False

        # Set the starting player
        if starting_player == "player":
            self.turn = 0
        elif starting_player == "ai":
            self.turn = 1
        else:
            raise ValueError("Invalid starting player. Choose 'player' or 'ai'.")

    def create_board(self):
        return np.zeros((self.config.ROW_COUNT, self.config.COLUMN_COUNT))

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(self, board, col):
        return board[self.config.ROW_COUNT - 1][col] == 0

    def get_next_open_row(self, board, col):
        for r in range(self.config.ROW_COUNT):
            if board[r][col] == 0:
                return r

    def print_board(self, board):
        print(np.flip(board, 0))

    def winning_move(self, board, piece):
        for c in range(self.config.COLUMN_COUNT - 3):
            for r in range(self.config.ROW_COUNT):
                if all([board[r][c + i] == piece for i in range(self.config.WINDOW_LENGTH)]):
                    return True
        for c in range(self.config.COLUMN_COUNT):
            for r in range(self.config.ROW_COUNT - 3):
                if all([board[r + i][c] == piece for i in range(self.config.WINDOW_LENGTH)]):
                    return True
        for c in range(self.config.COLUMN_COUNT - 3):
            for r in range(self.config.ROW_COUNT - 3):
                if all([board[r + i][c + i] == piece for i in range(self.config.WINDOW_LENGTH)]):
                    return True
        for c in range(self.config.COLUMN_COUNT - 3):
            for r in range(3, self.config.ROW_COUNT):
                if all([board[r - i][c + i] == piece for i in range(self.config.WINDOW_LENGTH)]):
                    return True

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = self.config.PLAYER_PIECE if piece == self.config.AI_PIECE else self.config.AI_PIECE
        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 2
        if window.count(opp_piece) == 3 and window.count(0) == 1:
            score -= 4
        return score

    def score_position(self, board, piece):
        score = 0
        center_array = [int(i) for i in list(board[:, self.config.COLUMN_COUNT // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3
        for r in range(self.config.ROW_COUNT):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(self.config.COLUMN_COUNT - 3):
                window = row_array[c:c + self.config.WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)
        for c in range(self.config.COLUMN_COUNT):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(self.config.ROW_COUNT - 3):
                window = col_array[r:r + self.config.WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)
        for r in range(self.config.ROW_COUNT - 3):
            for c in range(self.config.COLUMN_COUNT - 3):
                window = [board[r + i][c + i] for i in range(self.config.WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)
        for r in range(self.config.ROW_COUNT - 3):
            for c in range(self.config.COLUMN_COUNT - 3):
                window = [board[r + 3 - i][c + i] for i in range(self.config.WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)
        return score

    def is_terminal_node(self, board):
        return self.winning_move(board, self.config.PLAYER_PIECE) or \
               self.winning_move(board, self.config.AI_PIECE) or \
               len(self.get_valid_locations(board)) == 0

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        valid_locations = self.get_valid_locations(board)
        is_terminal = self.is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.winning_move(board, self.config.AI_PIECE):
                    return (None, 100000000000000)
                elif self.winning_move(board, self.config.PLAYER_PIECE):
                    return (None, -10000000000000)
                else:
                    return (None, 0)
            else:
                return (None, self.score_position(board, self.config.AI_PIECE))
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_open_row(board, col)
                b_copy = board.copy()
                self.drop_piece(b_copy, row, col, self.config.AI_PIECE)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value
        else:
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_open_row(board, col)
                b_copy = board.copy()
                self.drop_piece(b_copy, row, col, self.config.PLAYER_PIECE)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def get_valid_locations(self, board):
        valid_locations = []
        for col in range(self.config.COLUMN_COUNT):
            if self.is_valid_location(board, col):
                valid_locations.append(col)
        return valid_locations

    def pick_best_move(self, board, piece):
        valid_locations = self.get_valid_locations(board)
        best_score = -10000
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = self.get_next_open_row(board, col)
            temp_board = board.copy()
            self.drop_piece(temp_board, row, col, piece)
            score = self.score_position(temp_board, piece)
            if score > best_score:
                best_score = score
                best_col = col
        return best_col

    def draw_board(self, board):
        for c in range(self.config.COLUMN_COUNT):
            for r in range(self.config.ROW_COUNT):
                pygame.draw.rect(self.screen, self.BLUE, (c * self.SQUARESIZE, r * self.SQUARESIZE + self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE))
                pygame.draw.circle(self.screen, self.BLACK, (int(c * self.SQUARESIZE + self.SQUARESIZE / 2), int(r * self.SQUARESIZE + self.SQUARESIZE + self.SQUARESIZE / 2)), self.RADIUS)
        for c in range(self.config.COLUMN_COUNT):
            for r in range(self.config.ROW_COUNT):        
                if self.board[r][c] == self.config.PLAYER_PIECE:
                    pygame.draw.circle(self.screen, self.RED, (int(c * self.SQUARESIZE + self.SQUARESIZE / 2), self.height - int(r * self.SQUARESIZE + self.SQUARESIZE / 2)), self.RADIUS)
                elif self.board[r][c] == self.config.AI_PIECE: 
                    pygame.draw.circle(self.screen, self.YELLOW, (int(c * self.SQUARESIZE + self.SQUARESIZE / 2), self.height - int(r * self.SQUARESIZE + self.SQUARESIZE / 2)), self.RADIUS)
        pygame.display.update()

    def play(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.myfont = pygame.font.SysFont("monospace", 75)
        self.draw_board(self.board)
        pygame.display.update()

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, self.BLACK, (0, 0, self.width, self.SQUARESIZE))
                    posx = event.pos[0]
                    if self.turn == 0:
                        pygame.draw.circle(self.screen, self.RED, (posx, int(self.SQUARESIZE / 2)), self.RADIUS)

                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, self.BLACK, (0, 0, self.width, self.SQUARESIZE))
                    posx = event.pos[0]
                    col = int(math.floor(posx / self.SQUARESIZE))

                    if self.is_valid_location(self.board, col):
                        row = self.get_next_open_row(self.board, col)
                        self.drop_piece(self.board, row, col, self.config.PLAYER_PIECE)

                        if self.winning_move(self.board, self.config.PLAYER_PIECE):
                            label = self.myfont.render("You win!!", 1, self.RED)
                            self.screen.blit(label, (40, 10))
                            self.game_over = True

                        self.turn += 1
                        self.turn = self.turn % 2

                        self.draw_board(self.board)
                        pygame.display.update()

            if self.turn == 1 and not self.game_over:
                col, minimax_score = self.minimax(self.board, 5, -math.inf, math.inf, True)

                if self.is_valid_location(self.board, col):
                    row = self.get_next_open_row(self.board, col)
                    self.drop_piece(self.board, row, col, self.config.AI_PIECE)

                    if self.winning_move(self.board, self.config.AI_PIECE): 
                        label = self.myfont.render("AI wins!!", 1, self.YELLOW)
                        self.screen.blit(label, (40, 10))
                        self.game_over = True

                    self.draw_board(self.board)
                    pygame.display.update()

                    self.turn += 1
                    self.turn = self.turn % 2

            if self.game_over:
                pygame.time.wait(3000)

if __name__ == "__main__":
    starting_player = input("Who starts first? (player/ai): ").strip().lower()
    game = Connect4Game(starting_player=starting_player)
    game.play()
