#!/usr/bin/python

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

def router():
    print("Router")

def switch():
    print("Switch")

def mls():
    print("Multi Layer Switch")


root = Tk()
root.title("PacketTracer Config generator")
root.configure(background="lightblue")
root.minsize(500,300)

text = Label(root, text="Which device are you configuring?")
text.pack()

router = Button(root, text="Router", command=router)
router.pack()

switch = Button(root, text="Switch", command=switch)
switch.pack()

mls = Button(root, text="Multi Layer Switch", command=mls)
mls.pack()



root.mainloop()






top = tkinter.Tk()

