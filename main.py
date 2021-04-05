import tkinter as tk
from functools import partial
from grid import generateGrid,printGrid
import math
from tkinter.messagebox import showerror, showinfo

class Minesweeper:
    ROWS = 10
    COLUMNS = 10
    DIFFICULTY = 0.1
    BUTTON_HEIGHT = 30
    BUTTON_WIDTH = 40
    window = None

    gameGrid = []
    mineGrid = []
    openset=[]

    def __init__(self):
        self.interface = Interface()
        self.mineGrid = generateGrid(self.ROWS,self.COLUMNS,math.ceil((self.ROWS*self.COLUMNS)*self.DIFFICULTY))
        self.Game()

    def expand(self,i,j):
        rows = len(self.mineGrid)
        cols = len(self.mineGrid[0])
        if (i,j) in self.openset:
            return
        self.openset.append((i,j))
        print(self.gameGrid[i][j])
        if self.gameGrid[i][j].winfo_exists():
            self.gameGrid[i][j].destroy()
        if self.mineGrid[i][j] != ' ':
            l = tk.Label(self.window,text=self.mineGrid[i][j],fg="blue")
            l.place(x=i*self.BUTTON_HEIGHT,y = j*self.BUTTON_WIDTH,height=40,width=30)
            # l.config(borderwidth=1,relief="solid")
            l.config(fg = '#37d3ff',
                        bg = '#001d26',
                        highlightthickness=4, 
                        highlightcolor="#37d3ff", 
                        highlightbackground="#ffffff", 
                        borderwidth=3)
            self.gameGrid[i][j] = l
            return
        if i>0:
            self.expand(i-1,j)
        if i<rows-1:
            self.expand(i+1,j)
        if j>0:
            self.expand(i,j-1)
        if j<cols-1:
            self.expand(i,j+1)
        if i>0 and j>0:
            self.expand(i-1,j-1)
        if i>0 and j<cols-1:
            self.expand(i-1,j+1)
        if i<rows-1 and j>0:
            self.expand(i+1,j-1)
        if i<rows-1 and j<cols-1:
            self.expand(i+1,j+1)
        return

    def mark(self,button,i,j,event):
        if button['text'] == '#':
            button.config(text="")
        else:
            button.config(text="#")

    def reveal(self,button,i,j):
        if self.mineGrid[i][j]==' ':
            self.expand(i,j)
            return
        if self.mineGrid[i][j]=='*':
            for r in range(self.ROWS):
                for c in range(self.COLUMNS):
                    l = tk.Label(self.window,text=self.mineGrid[r][c],fg="blue")
                    l.place(x=r*self.BUTTON_HEIGHT,y = c*self.BUTTON_WIDTH,height=40,width=30)
                    l.config(fg = '#37d3ff',
                        bg = '#001d26',
                        highlightthickness=4, 
                        highlightcolor="#37d3ff", 
                        highlightbackground="#ffffff", 
                        borderwidth=3)
                    try:
                        self.gameGrid[r][c].pack_forget()
                    except:
                        pass
            showerror("Game Over!", "You stepped onto a mine")
            return
        l = tk.Label(self.window,text=self.mineGrid[i][j],fg="blue")
        # print(mineGrid)
        l.place(x=i*self.BUTTON_HEIGHT,y = j*self.BUTTON_WIDTH,height=40,width=30)
        # l.config(borderwidth=1,relief="solid")
        l.config(fg = '#37d3ff',
                        bg = '#001d26',
                        highlightthickness=4, 
                        highlightcolor="#37d3ff", 
                        highlightbackground="#ffffff", 
                        borderwidth=3)
        self.gameGrid[i][j] = l
        button.destroy()
        self.openset.append((i,j))
        print(i,j,self.mineGrid[i][j],len(self.openset))
        if len(self.openset) == (self.ROWS*self.COLUMNS) - (math.ceil((self.ROWS*self.COLUMNS)*self.DIFFICULTY)):
            for r in range(self.ROWS):
                for c in range(self.COLUMNS):
                    l = tk.Label(self.window,text=self.mineGrid[r][c],fg="blue")
                    l.place(x=r*self.BUTTON_HEIGHT,y = c*self.BUTTON_WIDTH,height=40,width=30)
                    l.config(fg = '#37d3ff',
                        bg = '#001d26',
                        highlightthickness=4, 
                        highlightcolor="#37d3ff", 
                        highlightbackground="#ffffff", 
                        borderwidth=3)
                    try:
                        self.gameGrid[r][c].pack_forget()
                    except:
                        pass
            showinfo("Congratulations!","You successfully uncovered all the mines!!")
            return
        return
        # print(openset)

    # buttons = [tk.Button(window,text=str(i)+str(j),command=action).grid(row=i,column=j) for i in range(10) for j in range(10)]

    def reset(self,event):
        try:
            self.window.exit()
        except:
            pass
        self.openset = []
        self.mineGrid = generateGrid(self.ROWS,self.COLUMNS,math.ceil((self.ROWS*self.COLUMNS)*self.DIFFICULTY))
        self.interface.deleteGame()
        self.interface.newGame()

    def Game(self):
        self.window = tk.Tk()
        self.window.configure(background = '#001d26')
        self.window.geometry('300x400+625+200')
        self.window.bind('n',self.reset)
        for i in range(self.ROWS):
            row = []
            for j in range(self.COLUMNS):
                button = tk.Button(self.window,relief = "raised")
                button.place(x=i*self.BUTTON_HEIGHT,y = j*self.BUTTON_WIDTH,height=40,width=30)
                button.config(command = partial(self.reveal,button,i,j))
                button.bind('<Button-3>', partial(self.mark,button,i,j))
                button.config(height = 2, width = 3,fg = '#37d3ff',bg = '#001d26')
                row.append(button)
            self.gameGrid.append(row)
        self.window.mainloop()

class Interface:
    def newGame(self):
        self.m = Minesweeper()
    def deleteGame(self):
        pass

control = Interface()
control.newGame()