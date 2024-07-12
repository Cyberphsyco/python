from tkinter import *

def english():
    window.destroy()
    def ok():
        new_window.destroy()
        window2 = Tk()
        window2.geometry("300x300")
        window2.configure(bg="cyan")
        label = Label(window2,text="\U0001F602\U0001F602 YOU ARE GAY \U0001F602\U0001F602",bg="cyan",font=("consolas",15))
        label.pack(pady=70)
        
        window2.mainloop()
        
        
    new_window = Tk()
    new_window.geometry("300x300")
    new_window.configure(bg="cyan")
    label = Label(new_window,text="WHO EVER MOVE FIRST IS GAY \U0001F608 \U0001F608",bg="cyan",font=("Twemoji",12))
    label.pack(pady=70)
    
    label2 = Label(new_window,text="Click ok \U0001F447",font=("consolas",10),bg="cyan")
    label2.pack()
    button = Button(new_window,text="ok",command=ok,font=("consolas",10))
    button.pack(pady=20)
    
    
    new_window.mainloop()


def spanish():
    window.destroy()
    def ok():
        new_window.destroy()
        window2 = Tk()
        window2.geometry("300x300")
        window2.configure(bg="cyan")
        label = Label(window2,text="\U0001F602\U0001F602 TÚ ERES GAY \U0001F602\U0001F602",bg="cyan",font=("consolas",15))
        label.pack(pady=70)
        
        
        window2.mainloop()
        
        
    new_window = Tk()
    new_window.geometry("300x300")
    new_window.configure(bg="cyan")
    label = Label(new_window,text="QUIEN MUEVA PRIMERO ES GAY \U0001F608 \U0001F608",bg="cyan",font=("Twemoji",12))
    label.pack(pady=70)
    
    label2 = Label(new_window,text="Presiona ok \U0001F447",font=("consolas",10),bg="cyan")
    label2.pack()
    button = Button(new_window,text="ok",command=ok,font=("consolas",10))
    button.pack(pady=20)
    
    
    new_window.mainloop()


window = Tk()
window.geometry("300x300")
window.configure(bg="cyan")
frame = Frame(window,bg="cyan")

label = Label(window,text="ENGLISH OR SPANISH", font=("inkfree",20),bg="cyan")
label.pack(pady=25)

eng = Button(frame,text="English",command=english,font=("consolas",15))
eng.grid(row=0,column=0,padx=25)

span = Button(frame,text="Spanish",command=spanish,font=("consolas",15))
span.grid(row=0,column=1,padx=25)

frame.pack(pady=50)
window.mainloop()