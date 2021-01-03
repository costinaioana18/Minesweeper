import random
import tkinter
import datetime
from datetime import time, date, datetime
from time import sleep
from tkinter import *

class Game:
    def __init__(self, tk):
        self.dimensionX = 4
        self.dimensionY = 4
        self.bombs = 5
        self.seconds_left=0
        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.frame2 = Frame(self.tk)
        self.frame2.pack()
        self.gameStarted=0


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
        self.timeLabel.grid(row=self.dimensionX, column=0, columnspan=self.dimensionY)
        self.bombLabel = tkinter.Label(self.frame, text="Bombs:")
        self.minesSP = Spinbox(self.frame, from_=1, to=20)
        self.minesSP.grid(row=self.dimensionX + 1, column=10, columnspan=self.dimensionX)
        self.bombLabel.grid(row=self.dimensionX+1, column=0, columnspan=self.dimensionX)
        self.sizeLabel = tkinter.Label(self.frame, text="Size:")
        self.sizeLabel.grid(row=self.dimensionX+2, column=0, columnspan=self.dimensionX)
        self.sizeSP = Spinbox(self.frame, from_=4, to=30)
        self.sizeSP.grid(row=self.dimensionX + 2, column=10, columnspan=self.dimensionX)
        self.timeLimitLabel = tkinter.Label(self.frame, text="Time limit:")
        self.timeLimitLabel.grid(row=self.dimensionX + 3, column=0, columnspan=self.dimensionX)
        self.timeEntry=tkinter.Entry(self.frame)
        self.timeEntry.grid(row=self.dimensionX + 3, column=10, columnspan=self.dimensionX)
        self.startBtn = tkinter.Button(self.frame, text="Start", command=self.start_game)
        self.startBtn.grid(row=self.dimensionX + 4, column=0, columnspan=self.dimensionX)

        # if(self.gameStarted):
        #     for i in range(self.dimensionX):
        #         for j in range(self.dimensionY):
        #             L = tkinter.Label(self.frame, text='    ', image = self.icons["plain"])
        #             L.grid(row=i, column=j)
        #             L.bind('<Button-1>', lambda e, i=i, j=j: self.on_click(i, j, e))
        #
        #     self.initialize()
        #     self.printBoard()

    def initialize(self):
        self.board = [[None] * self.dimensionX for _ in range(self.dimensionY)]
        self.revealed = [[None] * self.dimensionX for _ in range(self.dimensionY)]

        if self.gameStarted:
            for i in range(self.dimensionX):
                for j in range(self.dimensionY):
                    L = tkinter.Label(self.frame2, text='    ', image=self.icons["plain"])
                    L.grid(row=i, column=j)
                    L.bind('<Button-1>', lambda e, i=i, j=j: self.on_click(i, j, e))

            #self.printRevealed()


        for i in range(self.dimensionX):
            for j in range(self.dimensionY):
                self.board[i][j]=0
                self.revealed[i][j]=0

        self.setTheTable()
        self.printBoard()


    def setTheTable(self):

        print(self.bombs)
        for i in range(self.bombs):
            rx=random.randint(0,self.dimensionX-1)
            ry = random.randint(0, self.dimensionX - 1)
            print(' am pus bomba')
            self.board[rx][ry]=-1

        for i in range(self.dimensionX):
            for j in range(self.dimensionY):
                self.adiacentBombs(i,j)



    def printBoard(self):
        for i in range(self.dimensionX):
            print(self.board[i])

    def printRevealed(self):
        for i in range(self.dimensionX):
            print(self.revealed[i])



    def on_click(self,i, j, event):
        event.widget.config(image = self.icons["wrong"])
        self.revealed[i][j]=1;
        #self.printRevealed()
        #self.printBoard()


    def countdown(self):
        self.timeLabel['text'] = "Time left: " + str(self.seconds_left)

        if self.seconds_left:
            self.seconds_left -= 1
            #print(self.seconds_left)
            self.frame.after(1000, self.countdown)
        else:
            print('game over')

    def adiacentBombs(self,i,j):
        count=0;
        dx=[0,0,-1,-1,-1,1,1,1]
        dy=[1,-1,0,1,-1,-1,0,1]
        if self.board[i][j]==-1:
            return
        for c in range(8):
            if(i+dx[c]>=0 and i+dx[c]<self.dimensionX and j+dy[c]>=0 and j+dy[c]<self.dimensionY):
                if(self.board[i+dx[c]][j+dy[c]])==-1:
                    count+=1

        self.board[i][j]=count


    def start_game(self):

        #starting the countdown
        self.seconds_left = int(self.timeEntry.get())
        print(self.seconds_left)
        self.countdown()
        self.dimensionX=int(self.sizeSP.get())
        self.dimensionY=self.dimensionX
        print('size bombe')
        print(self.dimensionX)
        self.bombs=int(self.minesSP.get())
        print(self.bombs)
        self.gameStarted = 1

        self.initialize()



if __name__ == '__main__':
    window = Tk()
    window.title("Minesweeper")
    minesweeper = Game(window)
    window.mainloop()