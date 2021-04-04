import tkinter as tk

window = tk.Tk()

buttons = [tk.Button(window,text=str(i)+str(j)).grid(row=i,column=j) for i in range(10) for j in range(10)]
window.mainloop()