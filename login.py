from tkinter import *
from tkinter import messagebox


def open():
    
    global label2
    global label3
    guyyy = label2.get()
    brooo = label3.get()
    
    if label2.get() != "" and label3.get()!="" and label4.get()!="":
        if label3.get() == label4.get():
            messagebox.showinfo("Account creation","Acoount creation successful now login")
            new_window = Tk()
            new_window.geometry("440x500")
            new_window.configure(bg="#444455")
                

            opening2=Label(new_window,text="login",font=("consolas",25),bg="#444455",fg="#ff3300")
            opening2.pack(pady=25)



            frame2 = Frame(new_window,bg="#444455")
            frame2.pack(pady=10)


            enter_name2 = Label(frame2,text="username:",font=("consloas",15),bg="#444455",fg="white")
            enter_name2.grid(row=1,column=0)
            label22 = Entry(frame2,text="",font=("ink free",16))
            label22.grid(row = 1,column= 2, pady=5)
            
                        
            password2 = Label(frame2,text="password:",font=("consloas",15),bg="#444455",fg="white")
            password2.grid(row=2,column=-0)
            label33 = Entry(frame2,text="",show="*",font=("ink free",16))
            label33.grid(row = 2,column= 2, pady=5)
            
            
            def login():
                
                
                global label2
                global label3
                
                if label22.get() == guyyy and label33.get() == brooo:
                    info_label2.config(text="Login successful",fg="green")
                    messagebox.showinfo("login","login successful")
                                        
                elif label22.get() == guyyy and label33.get() != brooo:
                    info_label2.config(text="Incorrect password",fg="red")
                    messagebox.showerror("login error","Incorrect password")
                                        
                elif label22.get() != guyyy and label33.get() == brooo:
                    info_label2.config(text="Username not found",fg="red")
                    messagebox.showerror("login error","Username not found")
                                        
                elif label22.get() != guyyy and label33.get() != brooo:
                    info_label2.config(text="Invalid info",fg="red")
                    messagebox.showerror("login error","Invalid info")
                     
                     
                     
                     
                        
            button2 = Button(new_window,command=login,text="login",font=('ariel',15),height=2,fg="#ff3300")
            button2.pack(pady=25)
            
            
            info_label2 = Label(new_window,text="",font=("american typewriter",16),bg="#444455",fg="white")
            info_label2.pack()

            
            window.destroy()
    if label4.get() == "" and label3.get() == "" and label2.get() == "":
        messagebox.showerror("login error","Fill out the form")
    elif label3.get() != label4.get():
        info_label.config(text="Password do not match",fg="red")
        messagebox.showerror("login error","Password do not match")
    elif label2.get() == "":
        messagebox.showerror("login error","Username cannot be empty")
    elif label3.get() == "":
        messagebox.showerror("login error","Insert a password")
    elif label4.get() == "":
        messagebox.showerror("login error","Verify your password you dumbass")
               
               

        
window = Tk()
window.geometry("440x500")
window.configure(bg="#444455")


opening=Label(window,text="Create an account",font=("ink free",25),bg="#444455",fg="#ff3300")
opening.pack(pady=25)



frame = Frame(window,bg="#444455")
frame.pack(pady=10)


enter_name = Label(frame,text="Username:",font=("consloas",15),bg="#444455",fg="white")
enter_name.grid(row=1,column=0)
label2 = Entry(frame,text="",font=("ink free",16))
label2.grid(row = 1,column= 2, pady=5)



password = Label(frame,text="password:",font=("consloas",15),bg="#444455",fg="white")
password.grid(row=2,column=-0)
label3 = Entry(frame,text="",show="*",font=("ink free",16))
label3.grid(row = 2,column= 2, pady=5)


verify_password = Label(frame,text="Verify password:",font=("consloas",15),bg="#444455",fg="white")
verify_password.grid(row=3,column=0)
label4 = Entry(frame,text="",show="*",font=("ink free",16))
label4.grid(row = 3,column= 2, pady=5)



button = Button(window,command=open,text="create",font=('ariel',15),fg="#ff3300")
button.pack(pady=25)

info_label = Label(window,text="",font=("american typewriter",16),bg="#444455",fg="white")
info_label.pack()
window.mainloop()