from random import randint


class TicTacToeGame:
    def __init__(self):
        self.single_player_ind = None
        self.count = None
        self.is_x_turn = None
        self.board = None
        self.new_game(2)
        self.winning_conditions = [
            [(0, 0), (0, 1), (0, 2)],  # Row 1
            [(1, 0), (1, 1), (1, 2)],  # Row 2
            [(2, 0), (2, 1), (2, 2)],  # Row 3
            [(0, 0), (1, 0), (2, 0)],  # Column 1
            [(0, 1), (1, 1), (2, 1)],  # Column 2
            [(0, 2), (1, 2), (2, 2)],  # Column 3
            [(0, 0), (1, 1), (2, 2)],  # Diagonal 1
            [(0, 2), (1, 1), (2, 0)]   # Diagonal 2
        ]

    def make_move(self, row, col):
        if self.board[row][col] == '':
            if self.is_x_turn:
                self.board[row][col] = 'X'
            else:
                self.board[row][col] = 'O'

    def next_turn(self):
        self.is_x_turn = not self.is_x_turn
        self.count += 1

    def get_best_move(self):
        best_score = float('-inf')
        best_move = None

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    # Make the move on a temporary board
                    temp_board = [row[:] for row in self.board]
                    temp_board[row][col] = 'O'

                    # Evaluate the move using minimax
                    score = self.minimax(temp_board, 0, False)

                    # Update the best move if the score is higher
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        return best_move

    def minimax(self, board, depth, is_maximizing):
        result, line = self.win_check_temp(board, depth)
        if result == 'X':
            return -1
        elif result == 'O':
            return 1
        elif result == 'draw':
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = ''
                        best_score = min(score, best_score)
            return best_score

    def win_check(self):

        # Check for a win
        for condition in self.winning_conditions:
            symbols = [self.board[row][col] for row, col in condition]
            if symbols[0] == symbols[1] == symbols[2] != '':
                return symbols[0], condition

        # Check for a draw
        if self.count == 8:
            return 'draw', None

        return None, None

    def win_check_temp(self, board, depth):

        # Check for a win
        for condition in self.winning_conditions:
            symbols = [board[row][col] for row, col in condition]
            if symbols[0] == symbols[1] == symbols[2] != '':
                return symbols[0], condition

        # Check for a draw
        if self.count + depth == 8:
            return 'draw', None

        return None, None

    def new_game(self, players):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.is_x_turn = True
        self.count = 0
        if players == 1:
            self.single_player_ind = True
        else:
            self.single_player_ind = False
