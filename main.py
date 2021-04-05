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
    print("Minegrid["+str(i)+"]["+str(j)+"] : "+mineGrid[i][j]+".")
    if mineGrid[i][j] != ' ':
        print(i,j)
        l = tk.Label(window,text=mineGrid[i][j],fg="blue")
        l.place(x=i*BUTTON_HEIGHT,y = j*BUTTON_WIDTH)
        l.config(height = 3, width = 3)
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

def action(button,i,j):
    if mineGrid[i][j]==' ':
        expand(i,j)
        return
    l = tk.Label(window,text=mineGrid[i][j],fg="blue")
    # print(mineGrid)
    l.place(x=i*BUTTON_HEIGHT,y = j*BUTTON_WIDTH)
    l.config(height = 2, width = 3)
    gameGrid[i][j] = l
    button.destroy()
    # print(openset)

# buttons = [tk.Button(window,text=str(i)+str(j),command=action).grid(row=i,column=j) for i in range(10) for j in range(10)]
for i in range(ROWS):
    row = []
    for j in range(COLUMNS):
        button = tk.Button(window,text=str(i)+str(j),relief = "raised")
        button.place(x=i*BUTTON_HEIGHT,y = j*BUTTON_WIDTH)
        button.config(command = partial(action,button,i,j))
        button.config(height = 2, width = 3)
        row.append(button)
    gameGrid.append(row)
printGrid(mineGrid)

window.mainloop()