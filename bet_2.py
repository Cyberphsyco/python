from tkinter import *
import random
from tkinter import messagebox
import string

amounts = int(100000)

games = ["England(1.54) vs Germany(5.00)\n 1 X 2","Spain(3.00) vs Russia(2.00)\n 1 X 2"]
game = random.choice(games)

def bets():
    global amounts
        
    if guess.get() == "":
        messagebox.showerror("error","input a valid odd")
    
    else:
        
        if int(entry.get()) > int(amounts):
            messagebox.showerror("Error","insufficent fund")
            entry.delete(0,END)
        elif int(entry.get()) == int(amounts):
            messagebox.showinfo("Bet","bet placed")
            amounts -= int(entry.get())
            amount.config(text=f"Balance: ${amounts}")
        
        else:
            if entry.get() != "":
                messagebox.showinfo("Bet","bet placed")
                amounts -= int(entry.get())
                amount.config(text=f"Balance: ${amounts}")

        
def submit():    
    list1 = ["1.54","5.00","1.54","5.00","1.54","5.00"]
    rand1 = random.choice(list1)
    
    list2 = ["2.00","3.00","2.00","3.00","2.00","3.00"]
    rand2 = random.choice(list2)
    
    if entry.get() == '':
        messagebox.showerror("Bet error","Place a bet")
    
        
    if int(entry.get()) > int(amounts) or int(entry.get()) < 0:
        messagebox.showerror("Error","Place a valid bet")
    else:
        if  str(guess.get()) == "1.54" and rand1 == "1.54" :
            gain = int(entry.get()) * 1.54
            messagebox.showinfo("congratulation",f"You won ${gain}")
            total = amounts + gain
            amount.config(text=f"Balance: ${total}")
                
        elif  str(guess.get()) == "5.00"  and rand1 == "5.00" :
            gain = int(entry.get()) * 5.00
            messagebox.showinfo("congratulation",f"You won ${gain}")
            total = amounts + gain
            amount.config(text=f"Balance: ${total}")
            
        elif  str(guess.get()) == "2.00" and rand2 == "2.00" :
            gain = int(entry.get()) * 2.00
            messagebox.showinfo("congratulation",f"You won ${gain}")
            total = amounts + gain
            amount.config(text=f"Balance: ${total}")
                
        elif  str(guess.get()) == "3.00"  and rand2 == "3.00" :
            gain = int(entry.get()) * 3.00
            messagebox.showinfo("congratulation",f"You won ${gain}")
            total = amounts + gain
            amount.config(text=f"Balance: ${total}")
        else:  
            messagebox.showerror("congratulation",f"You lost ${entry.get()}")
            amount.config(text=f"Balance: ${amounts}")
            
            
def reset():
    global game
    guess.delete(0,END)
    entry.delete(0,END)
    reset = random.choice(games)
    label.config(text=reset)

window = Tk()
window.geometry("400x500")
frame = Frame(window)
title = Label(window,text="PLUTO BET",font=("inkfree",30))
title.pack()

amount = Label(window,text=f"Balance: ${amounts}",font=("consolas",15))
amount.place(x=-1,y=60)

label =Label(frame,text=game,font=("consolas",15))
label.grid(row=1,columnspan=5,pady=20)

guess = Entry(frame,text="")
guess.grid(row=2,columnspan=2)


place = Label(frame,text="Enter amount to bet here:",font=("consolas",12))
place.grid(row=3,column=0,pady=20)

entry = Entry(frame,width=5,text="")
entry.grid(row=3,column=1,pady=20)

bet = Button(frame,text="place",command=bets,)
bet.grid(row=4,columnspan=2)


frame.pack(pady=70)

submits = Button(window,text="check",command=submit)
submits.pack()

resets = Button(window,text="Reset bet",command=reset)
resets.pack()
window.mainloop()