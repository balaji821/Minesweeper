import tkinter as tk

window = tk.Tk()
i = 0
j = 0
buttons = []

def action():
    global i
    print(buttons)
    i += 1
    buttons[i][j].destroy()

# buttons = [tk.Button(window,text=str(i)+str(j),command=action).grid(row=i,column=j) for i in range(10) for j in range(10)]
for i in range(10):
    for j in range(10):
        button = tk.Button(window,text=str(i)+str(j))
        button.grid(row=i,column=j)
        button.config(command = button.destroy)
i = 0
j = 0

window.mainloop()