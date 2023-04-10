from tkinter import*
import os
from PIL import Image,ImageTk
from tkinter import messagebox
from course import  courseC
from student import  studentC
from result import resultC
from report import view_class
import sqlite3
class RMS:

    def __init__(self,root):
         self.root=root
         self.root.title("Student Result Management System")
         self.root.geometry("1450x700+0+0")
         self.root.config(bg="#A2C7D4")

         self.logo_dash=ImageTk.PhotoImage(file="images/logo_1.png")

         title=Label(self.root,text="Student  Result Management",padx=5,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#123456",fg="#DADBDD").place(x=0,y=0,relwidth=1,height=50)
         M_Frame=LabelFrame(self.root,text="Menu",font=("san francisco",15),bd=5,bg="#F7f97d")
         M_Frame.place(x=150,y=70,width=545,height=80)

         Ex_Frame=LabelFrame(self.root,text="Exit",font=("san francisco",15),bd=5,bg="#F7f97d")
         Ex_Frame.place(x=695,y=70,width=505,height=80)

         R_Frame=LabelFrame(self.root,text="Result",font=("san francisco",15),bd=5,bg="#F7f97d")
         R_Frame.place(x=150,y=180,width=300,height=445)

        #buttons
         btn_course= Button(M_Frame,text="Course",font=("goudy old stle",15,"bold"),bg="#790FB7",fg="white",activeforeground="#7df9e5",activebackground="#Be7df9",cursor="hand2",command=self.add_course).place(x=60,y=3,width=200,height=40)
         btn_student= Button(M_Frame,text="Student",font=("goudy old stle",15,"bold"),bg="#790FB7",fg="white",activeforeground="#7df9e5",activebackground="#Be7df9",cursor="hand2",command=self.add_student).place(x=290,y=3,width=200,height=40)
         btn_logout= Button(Ex_Frame,text="Logout",font=("goudy old stle",15,"bold"),bg="#790FB7",fg="white",activeforeground="#7df9e5",activebackground="#Be7df9",cursor="hand2",command=self.logout).place(x=35,y=3,width=200,height=40)
         btn_exit= Button(Ex_Frame,text="Exit",font=("goudy old stle",15,"bold"),bg="#790FB7",fg="white",activeforeground="red",activebackground="#Be7df9",cursor="hand2",command=self.exit_).place(x=265,y=3,width=200,height=40)

         btn_uploadResult= Button(R_Frame,text="Add Result",font=("goudy old stle",15,"bold"),bg="#790FB7",fg="white",activeforeground="#7df9e5",activebackground="#Be7df9",cursor="hand2",command=self.add_result).place(x=20,y=50,width=250,height=70)
         btn_viewResult= Button(R_Frame,text="View Result",font=("goudy old stle",15,"bold"),bg="#790FB7",fg="white",activeforeground="#7df9e5",activebackground="#Be7df9",cursor="hand2",command=self.view_report).place(x=20,y=250,width=250,height=70)

         #content of window
         self.bg_img=Image.open("images/books.jpg")
         self.bg_img=self.bg_img.resize((930,400),Image.ANTIALIAS)
         self.bg_img=ImageTk.PhotoImage(self.bg_img)

         self.lbl_img=Label(self.root,image=self.bg_img).place(x=500,y=180,width=700,height=340)

         self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old stle",15),bd=10,bg="#D4c039",fg="white")
         self.lbl_course.place(x=550,y=530,width=280,height=90)
         self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old stle",15),bd=10,bg="#D4c039",fg="white")
         self.lbl_student.place(x=860,y=530,width=280,height=90)

         footer=Label(self.root,text="Student  Result Management\nContact for any issues : 9999999999",font=("goudy old style",12),bg="#464444",fg="white").pack(side=BOTTOM,fill=X)
         self.details()


    def details(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course ")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            
            cur.execute("select * from student ")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
            
            self.lbl_course.after(200,self.details)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=courseC(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentC(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultC(self.new_win)

    def view_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=view_class(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")


    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()


if __name__== "__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
