import tkinter as tk
from functools import partial
from grid import generateGrid,printGrid
import math

ROWS = 10
COLUMNS = 10
DIFFICULTY = 0.1
BUTTON_HEIGHT = 30
BUTTON_WIDTH = 40


window = tk.Tk()
window.configure(background = '#001d26')
window.geometry('300x400')
gameGrid = []
mineGrid = generateGrid(ROWS,COLUMNS,math.ceil((ROWS*COLUMNS)*DIFFICULTY))
openset=[]

def expand(i,j):
    rows = len(mineGrid)
    cols = len(mineGrid[0])
    if (i,j) in openset:
        return
    openset.append((i,j))
    gameGrid[i][j].destroy()
    if mineGrid[i][j] != ' ':
        l = tk.Label(window,text=mineGrid[i][j],fg="blue")
        l.place(x=i*BUTTON_HEIGHT,y = j*BUTTON_WIDTH,height=40,width=30)
        # l.config(borderwidth=1,relief="solid")
        l.config(fg = '#37d3ff',
                    bg = '#001d26',
                    highlightthickness=4, 
                    highlightcolor="#37d3ff", 
                    highlightbackground="#ffffff", 
                    borderwidth=3)
        gameGrid[i][j] = l
        return
    if i>0:
        expand(i-1,j)
    if i<rows-1:
        expand(i+1,j)
    if j>0:
        expand(i,j-1)
    if j<cols-1:
        expand(i,j+1)
    if i>0 and j>0:
        expand(i-1,j-1)
    if i>0 and j<cols-1:
        expand(i-1,j+1)
    if i<rows-1 and j>0:
        expand(i+1,j-1)
    if i<rows-1 and j<cols-1:
        expand(i+1,j+1)
    return

def mark(button,i,j,event):
    if button['text'] == '#':
        button.config(text="")
    else:
        button.config(text="#")

def reveal(button,i,j):
    if mineGrid[i][j]==' ':
        expand(i,j)
        return
    l = tk.Label(window,text=mineGrid[i][j],fg="blue")
    # print(mineGrid)
    l.place(x=i*BUTTON_HEIGHT,y = j*BUTTON_WIDTH,height=40,width=30)
    # l.config(borderwidth=1,relief="solid")
    l.config(fg = '#37d3ff',
                    bg = '#001d26',
                    highlightthickness=4, 
                    highlightcolor="#37d3ff", 
                    highlightbackground="#ffffff", 
                    borderwidth=3)
    gameGrid[i][j] = l
    button.destroy()
    # print(openset)

# buttons = [tk.Button(window,text=str(i)+str(j),command=action).grid(row=i,column=j) for i in range(10) for j in range(10)]
for i in range(ROWS):
    row = []
    for j in range(COLUMNS):
        button = tk.Button(window,relief = "raised")
        button.place(x=i*BUTTON_HEIGHT,y = j*BUTTON_WIDTH,height=40,width=30)
        button.config(command = partial(reveal,button,i,j))
        button.bind('<Button-3>', partial(mark,button,i,j))
        button.config(height = 2, width = 3,fg = '#37d3ff',bg = '#001d26')
        row.append(button)
    gameGrid.append(row)

window.mainloop()