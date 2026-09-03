from tkinter import *
from time import strftime

v = Tk()
v.title("Reloj")

l = Label(v,font=("Arial",40), fg=("black"))
l.pack(padx=20,pady=20)

def reloj():
    l.config(text=strftime("%H:%M:%S"))
    l.after(1000,reloj)

reloj()
v.mainloop()