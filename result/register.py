from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import os
import sqlite3
class register:

    def __init__(self,root):
         self.root=root
         self.root.title("Registration Form")
         self.root.geometry("650x550+350+100")
         self.root.config(bg="#333333")
         self.root.focus_force()

    

         title=Label(self.root,text="Register Here",font=("times new roman",26,"bold"),bg="#333333",fg="#ff3399").place(x=0,y=15,width=650,height=40)
         
         
         f_name=Label(self.root,text="*First Name",font=("times new roman",18,"bold"),bg="#333333",fg="white").place(x=50,y=100)
         self.txt_fname=Entry(self.root,font=("times new roman",18),bg="lightgray")
         self.txt_fname.place(x=50,y=130,width=240)
         
         l_name=Label(self.root,text="Last Name",font=("times new roman",18,"bold"),bg="#333333",fg="white").place(x=370,y=100)
         self.txt_lname=Entry(self.root,font=("times new roman",18),bg="lightgray")
         self.txt_lname.place(x=370,y=130,width=240)

         contact=Label(self.root,text="*Contact  No.",font=("times new roman",18,"bold"),bg="#333333",fg="white").place(x=50,y=170)
         self.txt_contact=Entry(self.root,font=("times new roman",18),bg="lightgray")
         self.txt_contact.place(x=50,y=200,width=240)

         email=Label(self.root,text="*Email",font=("times new roman",18,"bold"),bg="#333333",fg="white").place(x=370,y=170)
         self.txt_email=Entry(self.root,font=("times new roman",18),bg="lightgray")
         self.txt_email.place(x=370,y=200,width=240)

         password=Label(self.root,text="*Password",font=("times new roman",18,"bold"),bg="#333333",fg="white").place(x=50,y=240)
         self.txt_password=Entry(self.root,font=("times new roman",18),bg="lightgray",show="•")
         self.txt_password.place(x=50,y=270,width=240)

         show_btn=Checkbutton(self.root,text="show password",cursor="hand2",bg="#333333",fg="white",activebackground="#333333",command=self.show_password)
         show_btn.place(x=60,y=310)

         cpassword=Label(self.root,text="*Confirm Password",font=("times new roman",18,"bold"),bg="#333333",fg="white").place(x=370,y=240)
         self.txt_cpassword=Entry(self.root,font=("times new roman",18),bg="lightgray",show="•")
         self.txt_cpassword.place(x=370,y=270,width=240)


         
         btn_reg=Button(self.root,text="Register Now →",font=("San Francisco",18),bg="#0e9e18",fg="white",bd=0,cursor="hand2",command=self.register_data).place(x=220,y=400,height=35,width=200)

         btn_login=Button(self.root,text="Sign In",font=("times new roman",18),bg="#ff3399",fg="white",bd=0,cursor="hand2",command=self.login_window).place(x=220,y=452,height=35,width=200)

         
    def show_password(self):
        if self.txt_password.cget('show') and self.txt_cpassword.cget('show'):
            self.txt_password.config(show='')
            self.txt_cpassword.config(show='')
        else:
            self.txt_password.config(show='•')
            self.txt_cpassword.config(show='•')

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","Fill out all entry fields.\n(Last Name is Optional)",parent=self.root)

        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Passwords did not match",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="result.db")
                cur=con.cursor()
                cur.execute("select * from register where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist.Try with another Email",parent=self.root)
                else:
                    if len(self.txt_password.get())>=8 and len(self.txt_password.get())<=16 :

                        cur.execute("insert into register(f_name,l_name,contact,email,password) values(?,?,?,?,?)",
                            (self.txt_fname.get(),
                            self.txt_lname.get(),
                            self.txt_contact.get(),
                            self.txt_email.get(),
                            self.txt_password.get(),
                        
                        ))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Sucess","Register Successful",parent=self.root)
                        self.clear()
                        self.login_window()
                    else:
                        messagebox.showerror("Error","Password must be 8-16 characters")
            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}") 

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)


    
        



        



if __name__== "__main__":
    root=Tk()
    obj=register(root)
    root.mainloop()