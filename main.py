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
        self.won=0
        self.gameStarted=0
        self.gameRestarted=0
        self.beginning = datetime.now()
        self.counter = 0
        self.icons = {
            "plain": PhotoImage(file="icons/tile_plain.gif"),
            "clicked": PhotoImage(file="icons/tile_clicked.gif"),
            "mine": PhotoImage(file="icons/tile_mine.gif"),
            "flag": PhotoImage(file="icons/tile_flag.gif"),
            "wrong": PhotoImage(file="icons/tile_wrong.gif"),
            "one": PhotoImage(file="icons/1.gif"),
            "two": PhotoImage(file="icons/2.gif"),
            "three": PhotoImage(file="icons/3.gif"),
            "four": PhotoImage(file="icons/4.gif"),
            "five": PhotoImage(file="icons/5.gif"),
            "six": PhotoImage(file="icons/6.gif"),
            "seven": PhotoImage(file="icons/7.gif"),
            "eight": PhotoImage(file="icons/8.gif"),
        }
        self.timeLabel=tkinter.Label(self.frame, text = "Time left: unset")
        self.timeLabel.grid(row=self.dimensionX, column=0, columnspan=self.dimensionY)
        self.bombLabel = tkinter.Label(self.frame, text="Bombs:")
        self.minesSP = Spinbox(self.frame, from_=1, to=40)
        self.minesSP.grid(row=self.dimensionX + 1, column=10, columnspan=self.dimensionX)
        self.bombLabel.grid(row=self.dimensionX+1, column=0, columnspan=self.dimensionX)
        self.sizeLabel = tkinter.Label(self.frame, text="Size x:")
        self.sizeLabel.grid(row=self.dimensionX+2, column=0, columnspan=self.dimensionX)
        self.sizeSP = Spinbox(self.frame, from_=4, to=30)
        self.sizeSP.grid(row=self.dimensionX + 2, column=10, columnspan=self.dimensionX)

        self.sizeLabel2 = tkinter.Label(self.frame, text="Size y:")
        self.sizeLabel2.grid(row=self.dimensionX + 3, column=0, columnspan=self.dimensionX)
        self.sizeSP2 = Spinbox(self.frame, from_=4, to=30)
        self.sizeSP2.grid(row=self.dimensionX + 3, column=10, columnspan=self.dimensionX)

        self.timeLimitLabel = tkinter.Label(self.frame, text="Time limit:")
        self.timeLimitLabel.grid(row=self.dimensionX + 4, column=0, columnspan=self.dimensionX)
        self.timeEntry=tkinter.Entry(self.frame)
        self.timeEntry.grid(row=self.dimensionX + 4, column=10, columnspan=self.dimensionX)
        self.startBtn = tkinter.Button(self.frame, text="Start", command=self.start_game)
        self.startBtn.grid(row=self.dimensionX + 5, column=0, columnspan=self.dimensionX)

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
        self.frame2 = Frame(self.tk)
        self.frame2.pack()
        print("dimensiuni")
        print(self.dimensionX)
        print(self.dimensionY)
        self.board = [[None] * self.dimensionY for _ in range(self.dimensionX)]
        self.revealed = [[None] * self.dimensionY for _ in range(self.dimensionX)]
        self.flagged = [[None] * self.dimensionY for _ in range(self.dimensionX)]
        self.squares=[[None] * self.dimensionY for _ in range(self.dimensionX)]
        print(self.squares)
        if self.gameStarted:
            for i in range(self.dimensionX):
                for j in range(self.dimensionY):
                    print("dimensiuni")
                    print(self.dimensionX)
                    print(self.dimensionY)
                    self.squares[i][j] = tkinter.Label(self.frame2, text='    ', image=self.icons["plain"])
                    self.squares[i][j].grid(row=i, column=j)
                    self.squares[i][j].bind('<Button-1>', lambda e, i=i, j=j: self.on_click(i, j, e))
                    self.squares[i][j].bind('<Button-3>', lambda e, i=i, j=j: self.right_click(i, j, e))

            #self.printRevealed()


        for i in range(self.dimensionX):
            for j in range(self.dimensionY):
                self.board[i][j]=0
                self.revealed[i][j]=0

        self.setTheTable()

        #self.printBoard()
        #self.printRevealed()


    def setTheTable(self):

        print(self.bombs)
        for i in range(self.bombs):
            rx=random.randint(0,self.dimensionX-1)
            ry = random.randint(0, self.dimensionY - 1)
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
        #event.widget.config(image = self.icons["wrong"])
        self.revealed[i][j]=1;
        if(self.board[i][j]==-1):
            self.gameOverMine()
            self.squares[i][j].config(image=self.icons["wrong"])
            return

        #self.on_click( i+1, j, event)
        self.refreshBoard(i,j)
        self.printRevealed()
        if (self.getUnrevealed() == self.bombs and self.getFlagged() == self.bombs):
            print("am castigat am castigat")
            self.gameWon()
        #self.printRevealed()
        #self.printBoard()

    def right_click(self,i,j,event):
        print("right cli")
        if(self.revealed[i][j]==0):
            if(self.flagged[i][j]):
                self.squares[i][j].config(image=self.icons["plain"])
                self.flagged[i][j] = 0;
            else:
                self.squares[i][j].config(image=self.icons["flag"])
                self.flagged[i][j]=1;
        if(self.getUnrevealed()==self.bombs and self.getFlagged()==self.bombs):
            print("am castigat am castigat")
            self.gameWon()

    def refreshBoard(self,i,j):
        self.revealed[i][j]=1
        self.squares[i][j].config(image=self.icons["clicked"])
        self.setNumbers(i,j)
        if(self.board[i][j]>0):
            return
        if(self.board[i][j]==-1):
            self.squares[i][j].config(image=self.icons["mine"])
            return
        dx = [0, 0, -1, -1, -1, 1, 1, 1]
        dy = [1, -1, 0, 1, -1, -1, 0, 1]
        for c in range(8):
                if (i + dx[c] >= 0 and i + dx[c] < self.dimensionX and j + dy[c] >= 0 and j + dy[c] < self.dimensionY):
                    if(self.board[i+dx[c]][j+dy[c]]>=0 and self.board[i][j]==0):
                        self.squares[i+dx[c]][j+dy[c]].config(image=self.icons["clicked"])
                        self.setNumbers(i+dx[c],j+dy[c])
                        if(self.board[i+dx[c]][j+dy[c]]>=0 and self.revealed[i+dx[c]][j+dy[c]]==0):
                            self.refreshBoard(i+dx[c],j+dy[c])

    def countdown(self):
        if(self.won==0):
            self.timeLabel['text'] = "Time left: " + str(self.seconds_left)

            if self.seconds_left:
                self.seconds_left -= 1
                #print(self.seconds_left)
                self.frame.after(1000, self.countdown)
            else:
                print('game over')
                self.gameOverTime()

    def gameOverTime(self):
        self.timeLabel['text'] ="Game Over"
        for i in range(self.dimensionX):
            for j in range(self.dimensionY):
                self.setNumbers(i,j)
                if(self.board[i][j]==-1):
                    self.squares[i][j].config(image=self.icons["mine"])






    def gameOverMine(self):
        self.seconds_left = 0
        self.timeLabel['text'] = "Game Over"
        for i in range(self.dimensionX):
            for j in range(self.dimensionY):
                self.setNumbers(i, j)
                if (self.board[i][j] == -1):

                    self.squares[i][j].config(image=self.icons["mine"])

    def gameWon(self):
        self.won=1
        self.timeLabel['text'] = "You won"

    def setNumbers(self,i,j):
        if (self.board[i][j] == 0):
            self.squares[i][j].config(image=self.icons["clicked"])
        if(self.board[i][j]==1):
            self.squares[i][j].config(image=self.icons["one"])
        if (self.board[i][j] == 2):
            self.squares[i][j].config(image=self.icons["two"])
        if (self.board[i][j] == 3):
            self.squares[i][j].config(image=self.icons["three"])
        if (self.board[i][j] == 4):
            self.squares[i][j].config(image=self.icons["four"])
        if (self.board[i][j] == 5):
            self.squares[i][j].config(image=self.icons["five"])
        if (self.board[i][j] == 6):
            self.squares[i][j].config(image=self.icons["six"])
        if (self.board[i][j] == 7):
            self.squares[i][j].config(image=self.icons["seven"])
        if (self.board[i][j] == 8):
            self.squares[i][j].config(image=self.icons["eight"])

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

    def getUnrevealed(self):
        count=0
        for i in range(self.dimensionX):
            for j in range(self.dimensionY):
                if(self.revealed[i][j]==0):
                    count+=1
        return count

    def getFlagged(self):
        count=0
        for i in range(self.dimensionX):
            for j in range(self.dimensionY):
                if (self.flagged[i][j] == 1 and self.board[i][j]==-1):
                    count += 1
        return count


    def start_game(self):
        self.won=0
        #starting the countdown
        self.seconds_left = int(self.timeEntry.get())
        print(self.seconds_left)
        self.countdown()
        self.dimensionX=int(self.sizeSP.get())

        self.dimensionY=int(self.sizeSP2.get())
        print('size bombe')
        print(self.dimensionX)
        self.bombs=int(self.minesSP.get())
        print(self.bombs)
        self.gameStarted = 1
        if(self.gameRestarted):
            self.frame2.destroy()
        self.initialize()
        self.gameRestarted=1;




if __name__ == '__main__':
    window = Tk()
    window.title("Minesweeper")
    minesweeper = Game(window)
    window.mainloop()