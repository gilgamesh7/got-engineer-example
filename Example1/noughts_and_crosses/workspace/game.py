import tkinter as tk

class Game:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if not self.board[row][col]:
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != '':
                return True
        for col in range(len(self.board[0])):
            check_col = [row[col] for row in self.board]
            if check_col.count(check_col[0]) == len(check_col) and check_col[0] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if '' in row:
                return False
        return True
