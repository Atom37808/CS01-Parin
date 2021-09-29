from tkinter import *
root = Tk()
root.title("First GUI")
myText = Label(text="My name is",fg="blue",font=18).grid(row=0, column = 0)
myText = Label(text="Parin",fg="green",font=18).grid(row=1,column=1)
myText = Label(text="Kaewgunjai",fg="red",font=18).grid(row=2,column=2)
root.geometry("300x300")
root.mainloop()