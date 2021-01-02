import tkinter
import datetime
from datetime import time, date, datetime
from time import sleep
from tkinter import *
dimensionX=20
dimensionY=20
bombs=10
class Game:
    def __init__(self, tk):
        self.seconds_left=0
        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()

        self.board = [[None] * dimensionX for _ in range(dimensionY)]
        self.revealed = [[None] * dimensionX for _ in range(dimensionY)]
        self.beginning = datetime.now()
        self.counter = 0
        self.icons = {
            "plain": PhotoImage(file="icons/tile_plain.gif"),
            "clicked": PhotoImage(file="icons/tile_clicked.gif"),
            "mine": PhotoImage(file="icons/tile_mine.gif"),
            "flag": PhotoImage(file="icons/tile_flag.gif"),
            "wrong": PhotoImage(file="icons/tile_wrong.gif"),

        }
        self.timeLabel=tkinter.Label(self.frame, text = "Time left: unset")
        self.timeLabel.grid(row=dimensionX, column=0, columnspan=dimensionY)
        self.bombLabel = tkinter.Label(self.frame, text="Bombs:")
        self.minesSP = Spinbox(self.frame, from_=1, to=20)
        self.minesSP.grid(row=dimensionX + 1, column=10, columnspan=dimensionX)
        self.bombLabel.grid(row=dimensionX+1, column=0, columnspan=dimensionX)
        self.sizeLabel = tkinter.Label(self.frame, text="Size:")
        self.sizeLabel.grid(row=dimensionX+2, column=0, columnspan=dimensionX)
        self.sizeSP = Spinbox(self.frame, from_=4, to=30)
        self.sizeSP.grid(row=dimensionX + 2, column=10, columnspan=dimensionX)
        self.timeLimitLabel = tkinter.Label(self.frame, text="Time limit:")
        self.timeLimitLabel.grid(row=dimensionX + 3, column=0, columnspan=dimensionX)
        self.timeEntry=tkinter.Entry(self.frame)
        self.timeEntry.grid(row=dimensionX + 3, column=10, columnspan=dimensionX)
        self.startBtn = tkinter.Button(self.frame, text="Start", command=self.start_game)
        self.startBtn.grid(row=dimensionX + 4, column=0, columnspan=dimensionX)

        for i in range(dimensionX):
            for j in range(dimensionY):
                L = tkinter.Label(self.frame, text='    ', image = self.icons["plain"])
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


    def countdown(self):
        self.timeLabel['text'] = "Time left: " + str(self.seconds_left)

        if self.seconds_left:
            self.seconds_left -= 1
            print(self.seconds_left)
            self.frame.after(1000, self.countdown)
        else:
            print('game over')




    def start_game(self):
        self.seconds_left = int(self.timeEntry.get())
        print(self.seconds_left)
        self.countdown()



if __name__ == '__main__':
    window = Tk()
    window.title("Minesweeper")
    minesweeper = Game(window)
    window.mainloop()