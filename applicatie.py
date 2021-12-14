import tkinter
from tkinter import *


def open_steam():
    with open("steam.json") as f:
        firstline = f.readlines()[3].rstrip()
        return str(firstline)


def open_gui():
    win = tkinter.Tk()  # creating the main window and storing the window object in 'win'
    # We create the widgets here
    win.geometry('1000x500')
    frame = Frame(win)
    frame.pack()
    second_frame = Frame(win)
    second_frame.pack(side=BOTTOM)
    red_button = Button(frame, text=open_steam(), bg='red', fg='white')
    red_button.pack(side=LEFT)
    win.mainloop()  # running the loop that works as a trigger


open_gui()
