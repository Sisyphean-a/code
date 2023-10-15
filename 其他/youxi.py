# coding=utf-8 

import tkinter as tk

window=tk.Tk()
window.title("游戏")
window.geometry('400x300')
l=tk.Label(window,text='界面',bg='green',font=('Arial',12),width=30,height=2)
zh=tk.Entry(window,show=None,font=('Arial',12))
ma=tk.Entry(window,show='*',font=('Arial',12))

l.pack()
zh.pack()
ma.pack()

window.mainloop()

