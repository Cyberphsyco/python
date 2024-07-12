from tkinter import *

def entry(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_value.set(equation_text)
    
def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_value.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_value.set("math error")
        equation_text = ""
    except SyntaxError:
        equation_value.set("syntax error")
        equation_text = ""
def clear():
    global equation_text
    equation_value.set("")
    equation_text = ""


window = Tk()
window.geometry("500x550")
window.title("calculator")
equation_text = ""
equation_value = StringVar()

label = Label(window,width=35,height=4,font=("ariel",20),textvariable=equation_value,bg="white")
label.pack()
frame = Frame(window)
frame.pack()
button1 = Button(frame,text=1,height=3,width=6,font=("ariel",20),command=lambda: entry(1))
button1.grid(row=0,column=0)

button2 = Button(frame,text=2,height=3,width=6,font=("ariel",20),command=lambda: entry(2))
button2.grid(row=0,column=1)

button3 = Button(frame,text=3,height=3,width=6,font=("ariel",20),command=lambda: entry(3))
button3.grid(row=0,column=2)

button4 = Button(frame,text=4,height=3,width=6,font=("ariel",20),command=lambda: entry(4))
button4.grid(row=1,column=0)

button5 = Button(frame,text=5,height=3,width=6,font=("ariel",20),command=lambda: entry(5))
button5.grid(row=1,column=1)

button6 = Button(frame,text=6,height=3,width=6,font=("ariel",20),command=lambda: entry(6))
button6.grid(row=1,column=2)

button7 = Button(frame,text=7,height=3,width=6,font=("ariel",20),command=lambda: entry(7))
button7.grid(row=2,column=0)

button8 = Button(frame,text=8,height=3,width=6,font=("ariel",20),command=lambda: entry(8))
button8.grid(row=2,column=1)

button9 = Button(frame,text=9,height=3,width=6,font=("ariel",20),command=lambda: entry(9))
button9.grid(row=2,column=2)

button0 = Button(frame,text=0,height=3,width=6,font=("ariel",20),command=lambda: entry(0))
button0.grid(row=3,column=0)

decimal = Button(frame,text=".",height=3,width=6,font=("ariel",20),command=lambda: entry("."))
decimal.grid(row=3,column=1)

equal = Button(frame,text="=",height=3,width=6,font=("ariel",20),command=lambda: equals())
equal.grid(row=3,column=2)


addition = Button(frame,text="+",height=3,width=6,font=("ariel",20),command=lambda: entry("+"))
addition.grid(row=0,column=3)

minus = Button(frame,text="-",height=3,width=6,font=("ariel",20),command=lambda: entry("-"))
minus.grid(row=1,column=3)

multipy = Button(frame,text="*",height=3,width=6,font=("ariel",20),command=lambda: entry("*"))
multipy.grid(row=2,column=3)

divide = Button(frame,text="/",height=3,width=6,font=("ariel",20),command=lambda: entry("/"))
divide.grid(row=3,column=3)


delete = Button(window,text="clear",height=3,width=10,font=("ariel",20),command=clear)
delete.pack()
window.mainloop()