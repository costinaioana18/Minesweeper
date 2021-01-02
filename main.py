import tkinter
from tkinter import *
dimensionX=20
dimensionY=20
bombs=10
class Game:
    def __init__(self, tk):
        self.board = [[None] * dimensionX for _ in range(dimensionY)]
        self.revealed = [[None] * dimensionX for _ in range(dimensionY)]
        self.counter = 0
        self.icons = {
            "plain": PhotoImage(file="icons/tile_plain.gif"),
            "clicked": PhotoImage(file="icons/tile_clicked.gif"),
            "mine": PhotoImage(file="icons/tile_mine.gif"),
            "flag": PhotoImage(file="icons/tile_flag.gif"),
            "wrong": PhotoImage(file="icons/tile_wrong.gif"),

        }
        self.timeLabel=tkinter.Label(tk, text = "00:00:00")
        self.timeLabel.grid(row=dimensionX, column=0, columnspan=dimensionY)
        self.bombLabel = tkinter.Label(tk, text="Bombs:")
        self.bombLabel.grid(row=dimensionX+1, column=0, columnspan=dimensionX)
        self.sizeLabel = tkinter.Label(tk, text="Size:")
        self.sizeLabel.grid(row=dimensionX+2, column=0, columnspan=dimensionX)

        for i in range(dimensionX):
            for j in range(dimensionY):
                L = tkinter.Label(tk, text='    ', image = self.icons["plain"])
                L.grid(row=i, column=j)
                L.bind('<Button-1>', lambda e, i=i, j=j: self.on_click(i, j, e))

        self.initialize()
        self.printBoard()

    def initialize(self):
        for i in range(dimensionX):
            for j in range(dimensionY):
                self.board[i][j]=0
                self.revealed[i][j]=0



    def printBoard(self):
        for i in range(dimensionX):
            print(self.board[i])

    def printRevealed(self):
        for i in range(dimensionX):
            print(self.revealed[i])



    def on_click(self,i, j, event):
        event.widget.config(image = self.icons["wrong"])
        self.revealed[i][j]=1;
        #self.printRevealed()
        self.printBoard()


if __name__ == '__main__':
    window = Tk()
    window.title("Minesweeper")
    minesweeper = Game(window)
    window.mainloop()