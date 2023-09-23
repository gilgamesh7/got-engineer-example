from game import Game
from gui import GUI

def main():
    game = Game()
    gui = GUI(game)
    gui.start()

if __name__ == '__main__':
    main()
