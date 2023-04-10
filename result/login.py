from tkinter import*
import os
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class loginClass:

    def __init__(self,root):
         self.root=root
         self.root.title("Login Form")
         self.root.geometry("500x450+400+120")
         self.root.config(bg="#333333")
         self.root.focus_force()

    

         title=Label(self.root,text="Login Here",font=("times new roman",26,"bold"),bg="#333333",fg="#ff3399").place(x=0,y=15,width=500,height=40)


         email=Label(self.root,text="Email Address",font=("times new roman",18,"bold"),fg="white",bg="#333333",).place(x=50,y=90)
         self.txt_email=Entry(self.root,font=("times new roman",18),bg="lightgray")
         self.txt_email.place(x=50,y=130,width=350)

         password=Label(self.root,text="Password",font=("times new roman",18,"bold"),fg="white",bg="#333333",).place(x=50,y=180)
         self.txt_password=Entry(self.root,font=("times new roman",18),bg="lightgray",show="•")
         self.txt_password.place(x=50,y=220,width=350)

         show_btn=Checkbutton(self.root,text="show password",cursor="hand2",fg="white",bg="#333333",activebackground="#333333",command=self.show_password)
         show_btn.place(x=60,y=260)

         btn_register=Button(self.root,text="Register new Account?",font=("times new roman",15),bd=0,bg="#333333",fg="#0c14fb",activebackground="#333333",cursor="hand2",command=self.register_window).place(x=45,y=290)

         self.btn_login= Button(self.root,text="Login",font=("San Francisco",12,"bold"),bd=0,bg="#ff3399",fg="white",activebackground="#Fd514b",cursor="hand2",command=self.login)
         self.btn_login.place(x=180,y=350,width=140,height=35)


    def show_password(self):
        if self.txt_password.cget('show'):
            self.txt_password.config(show='')
        else:
            self.txt_password.config(show='•')


    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","Email or Password is not entered",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="result.db")
                cur=con.cursor()
                cur.execute("select * from register where email=? and password=?",(self.txt_email.get(),self.txt_password.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email or Password",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome {self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}") 

    
    def register_window(self):
        self.root.destroy()
        os.system("python register.py")





if __name__== "__main__":
    root=Tk()
    obj=loginClass(root)
    root.mainloop()