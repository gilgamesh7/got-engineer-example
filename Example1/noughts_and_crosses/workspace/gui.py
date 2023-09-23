import tkinter as tk
from game import Game

class GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()
        self.draw_board()

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                self.canvas.create_rectangle(i * 200, j * 200, (i + 1) * 200, (j + 1) * 200)
                if self.game.board[i][j] == 'X':
                    self.canvas.create_line(i * 200, j * 200, (i + 1) * 200, (j + 1) * 200)
                    self.canvas.create_line((i + 1) * 200, j * 200, i * 200, (j + 1) * 200)
                elif self.game.board[i][j] == 'O':
                    self.canvas.create_oval(i * 200, j * 200, (i + 1) * 200, (j + 1) * 200)

    def update_display(self):
        self.canvas.delete('all')
        self.draw_board()

    def handle_click(self, event):
        row = event.y // 200
        col = event.x // 200
        self.game.make_move(row, col)
        self.update_display()
        if self.game.check_win():
            print('Player ' + self.game.current_player + ' wins!')
            self.root.quit()
        elif self.game.check_draw():
            print('The game is a draw!')
            self.root.quit()

    def start(self):
        self.canvas.bind('<Button-1>', self.handle_click)
        self.root.mainloop()
