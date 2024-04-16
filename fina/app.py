from datetime import datetime 
import os
import time 
from time import strftime
import winsound
winsound.PlaySound
from tkinter import *

def alarm():
    import time
    b = y.get()  
    x = str(b)
    print(x) 
    stop = False
    while stop == False:
        time.sleep(1)
        now = datetime.now()
        rn = now.strftime("%H:%M:%S")
        print(rn)
        if rn >= x:
            stop = True
            winsound('alarm.mp3')

def time():
    string = strftime("%H:%M:%S") 
    L3.config(text = string)
    L3.after(1000,time)
top = Tk()
top.title("Alarm")
top.geometry("500x300")

y = IntVar()

L3 = Label(top, text="",font=("consolas,15"))
L1 = Label(top, text="Jam",font=("consolas,15"))
L1.pack( side = LEFT)
L3.pack( side = LEFT)
y = Entry(top, bd =6)
y.pack(side = RIGHT)

submit = Button(top,text = "Set Alarm",fg="black",bg="pink",width = 10,command = alarm).place(x =200,y=140)
time()
top.mainloop()