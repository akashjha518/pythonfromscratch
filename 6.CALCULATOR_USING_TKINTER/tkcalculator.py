from tkinter import *

window = Tk()
window.geometry('300x500')


e = Entry(window, width = 40, borderwidth=5)
e.place(x=0, y=0)


def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

b = Button(window, text='1', width=12, command = lambda:click(1))
b.place(x=10, y=60)

b = Button(window, text='2', width=12, command = lambda:click(2))
b.place(x=80, y=60)

b = Button(window, text='3', width=12, command = lambda:click(3))
b.place(x=170, y=60)

b = Button(window, text='4', width=12, command = lambda:click(4))
b.place(x=10, y=120)

b = Button(window, text='5', width=12, command = lambda:click(5))
b.place(x=80, y=120)

b = Button(window, text='6', width=12, command = lambda:click(6))
b.place(x=170, y=120)

b = Button(window, text='7', width=12, command = lambda:click(7))
b.place(x=10, y=180)

b = Button(window, text='8', width=12, command = lambda:click(8))
b.place(x=80, y=180)

b = Button(window, text='9', width=12, command = lambda:click(9))
b.place(x=170, y=180)

b = Button(window, text='0', width=12, command = lambda:click(0))
b.place(x=10, y=240)


def add():
    n1 = e.get()
    global math
    math = "add"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text='+', width=12, command= add)
b.place(x=80, y=240)


def sub():
    n1 = e.get()
    global math
    math = "sub"
    global i
    i= int(n1)
    e.delete(0, END)

b = Button(window, text='-', width=12, command= sub)
b.place(x=170, y=240)

def mul():
    n1 = e.get()
    global math
    math = "mul"
    global i
    i= int(n1)
    e.delete(0, END)

b = Button(window, text='*', width=12, command= mul)
b.place(x=10, y=300)

def div():
    n1 = e.get()
    global math
    math = "div"
    global i
    i= int(n1)
    e.delete(0, END)

b = Button(window, text='/', width=12, command= div)
b.place(x=80, y=300)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, i + int(n2))

    elif math == "sub":
        e.insert(0, i - int(n2))
    
    elif math == "mul":
        e.insert(0, i * int(n2))
    
    elif math == "div":
        e.insert(0, i / int(n2))


b = Button(window, text='=', width=12, command=equal)
b.place(x=170, y=300)

def clear():
    e.delete(0, END)
b = Button(window, text='clear', width=36, command= clear)
b.place(x=10, y=350)



mainloop()