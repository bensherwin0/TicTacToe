# Starts a game of Tic Tac Toe against the computer, printing the game in the terminal

from TTTGame import Game
from Player import getMove

if __name__ == "__main__":
    import Player as tp
    g = Game()
    counter = 0

    # Computer goes first
    # To go first instead, comment out this line
    g.player(tp.getMove(g))

    print(g)
    while(g.isOver() == " "):
        # Human input
        g.play()
        counter +=1
        print(g)
        if (counter < 9):
            # Computer input
            g.player(tp.getMove(g))
            counter += 1
            print(g)

    print("the winner is " + g.isOver())