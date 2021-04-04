import tkinter as tk
from functools import partial

window = tk.Tk()
gameGrid = []

def action(button,i,j):
    l = tk.Label(window,text=str(i)+str(j),fg="red")
    l.grid(row=i,column=j)
    gameGrid[i][j] = l
    button.destroy()

# buttons = [tk.Button(window,text=str(i)+str(j),command=action).grid(row=i,column=j) for i in range(10) for j in range(10)]
for i in range(10):
    row = []
    for j in range(10):
        button = tk.Button(window,text=str(i)+str(j))
        button.grid(row=i,column=j)
        button.config(command = partial(action,button,i,j))
        row.append(button)
    gameGrid.append(row)

window.mainloop()