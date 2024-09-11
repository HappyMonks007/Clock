from tkinter import * #for GUI interphase
from tkinter.ttk import * #for theme of the clock
from time import strftime # to change the time to text


root=Tk() #function to create window dialogie box
root.title("my clock")

#design with the help of Label function
label=Label(root,font=("ds.digital", 80),background="black", foreground="cyan")
label.pack(anchor="center")

def time():
    string=strftime("%H:%M:%S %p") #%p for AM or PM
    label.config(text=string)
    label.after(1000, time)
time()
mainloop()
