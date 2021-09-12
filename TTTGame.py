# A class containing the game board, current player, and methods to determine
#   if the game is over and to place a move

class Game:

    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.currPlayer = "X"
    
    def copy(self):
        g = Game()
        g.board = self.board.copy()
        g.currPlayer = self.currPlayer
        return g


    def play(self):
        number = int(input("enter a number 1-9: ")) - 1
        if (self.board[number] == " "): 
            self.board[number] = self.currPlayer
            if (self.currPlayer == "X"): self.currPlayer = "O"
            elif (self.currPlayer == "O"): self.currPlayer = "X"
            return True
        return False
    def player(self, number):
        if self.board[number] == " " and self.isOver() == " ": 
            self.board[number] = self.currPlayer
            if (self.currPlayer == "X"): self.currPlayer = "O"
            elif (self.currPlayer == "O"): self.currPlayer = "X"
            return True
        return False

    # returns "X" if the first player wins, "O" if the second wins, 
    #   "Nobody" if the game is a tie, and " " if the game is still in progress
    def isOver(self):
        if (self.board[0] == "X" and self.board[4] == "X" and self.board[8] == "X"): return "X"
        if (self.board[2] == "X" and self.board[4] == "X" and self.board[6] == "X"): return "X"
        if (self.board[2] == "O" and self.board[4] == "O" and self.board[6] == "O"): return "O"
        if (self.board[0] == "O" and self.board[4] == "O" and self.board[8] == "O"): return "O"
        xCounter = 0
        oCounter = 0
        for j in range(3):
            for i in range(3):
                if (self.board[3 * j + i] == "X"): xCounter += 1
                if self.board[3 * j + i] == "O": oCounter += 1
            if xCounter == 3: return "X"
            else: xCounter = 0
            if oCounter == 3: return "O"
            else: oCounter = 0
        for j in range(3):
            for i in range(3):
                if (self.board[3 * i + j] == "X"): xCounter += 1
                if self.board[3 * i + j] == "O": oCounter += 1
            if xCounter == 3: return "X"
            else: xCounter = 0
            if oCounter == 3: return "O"
            else: oCounter = 0
        for j in self.board:
            if j == " ": return " "
        return "Nobody"
                

    def __str__(self):
         s = " " + self.board[0] + " | " + self.board[1] + " | " + self.board[2] + " "
         s = s + "\n"
         s = s + "___________"
         s = s + "\n"
         s = s + " " + self.board[3] + " | " + self.board[4] + " | " + self.board[5] + " "
         s = s + "\n"
         s = s + "___________"
         s = s + "\n"
         s = s + " " + self.board[6] + " | " + self.board[7] + " | " + self.board[8] + " " + "\n"
         return s
