from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
class view_class:

    def __init__(self,root):
         self.root=root
         self.root.title("Student Result Management System")
         self.root.geometry("1000x430+80+50")
         self.root.config(bg="lightyellow")
         self.root.focus_force()

         self.var_search=StringVar()
         self.var_id=""

         title=Label(self.root,text="View Results",font=("goudy old style",20,"bold"),bg="#EE1019",fg="white").place(x=0,y=15,width=1000,height=35)


         lbl_studentSelect=Label(self.root,text="Search by Roll No. ",font=("goudy old style",18,"bold"),bg="lightyellow").place(x=200,y=70)
         txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",18,),bg="white").place(x=400,y=70,width=200)
         self.btn_search= Button(self.root,text="Search",font=("goudy old stle",12,),bg="lightblue",activebackground="blue",cursor="hand2",command=self.search)
         self.btn_search.place(x=620,y=70,width=70,height=30)
         self.btn_clear= Button(self.root,text="Clear",font=("goudy old stle",12,),bg="lightgray",activebackground="white",cursor="hand2",command=self.clear)
         self.btn_clear.place(x=700,y=70,width=70,height=30)


         lbl_roll=Label(self.root,text="Roll No",font=("goudy old style",18,"bold"),bg="white",bd=2,relief=GROOVE).place(x=80,y=200,width=140,height=50)
         lbl_name=Label(self.root,text="Name",font=("goudy old style",18,"bold"),bg="white",bd=2,relief=GROOVE).place(x=220,y=200,width=140,height=50)
         lbl_course=Label(self.root,text="Course",font=("goudy old style",18,"bold"),bg="white",bd=2,relief=GROOVE).place(x=360,y=200,width=140,height=50)
         lbl_marks=Label(self.root,text="Mark Obtained",font=("goudy old style",18,"bold"),bg="white",bd=2,relief=GROOVE).place(x=500,y=200,width=165,height=50)
         lbl_fullMark=Label(self.root,text="Total Mark",font=("goudy old style",18,"bold"),bg="white",bd=2,relief=GROOVE).place(x=665,y=200,width=140,height=50)
         lbl_percentage=Label(self.root,text="Percentage",font=("goudy old style",18,"bold"),bg="white",bd=2,relief=GROOVE).place(x=805,y=200,width=140,height=50)

         self.roll=Label(self.root,font=("goudy old style",18,"bold"),bg="white",bd=2,relief=GROOVE)
         self.roll.place(x=80,y=250,width=140,height=50)
         self.name=Label(self.root,font=("goudy old style",18,"bold"),bg="white",bd=2,relief=GROOVE)
         self.name.place(x=220,y=250,width=140,height=50)
         self.course=Label(self.root,font=("goudy old style",18,"bold"),bg="white",bd=2,relief=GROOVE)
         self.course.place(x=360,y=250,width=140,height=50)
         self.marks=Label(self.root,font=("goudy old style",18,"bold"),bg="white",bd=2,relief=GROOVE)
         self.marks.place(x=500,y=250,width=165,height=50)
         self.fullMark=Label(self.root,font=("goudy old style",18,"bold"),bg="white",bd=2,relief=GROOVE)
         self.fullMark.place(x=665,y=250,width=140,height=50)
         self.percentage=Label(self.root,font=("goudy old style",18,"bold"),bg="white",bd=2,relief=GROOVE)
         self.percentage.place(x=805,y=250,width=140,height=50)


         self.btn_goback= Button(self.root,text="⬅Go Back",font=("goudy old stle",12,),bg="green",fg="white",activebackground="lightgreen",cursor="hand2",command=self.goback)
         self.btn_goback.place(x=396,y=370,width=100,height=35)


         self.btn_delete= Button(self.root,text="Delete",font=("goudy old stle",12,),bg="Red",fg="white",activebackground="#Fd514b",cursor="hand2",command=self.delete)
         self.btn_delete.place(x=505,y=370,width=100,height=35)










    def search(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No required.",parent=self.root)
            else:
                cur.execute("select * from result where rollno=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row != None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.fullMark.config(text=row[5])
                    self.percentage.config(text=row[6])
                    x=row[6]
                    if float(x) >= 50.0:
                        messagebox.showinfo("Result","Student is PASSED",parent=self.root)
                    else:
                        messagebox.showinfo("Result","Student is FAILED",parent=self.root)
                else:
                    
                    messagebox.showerror("Error","No record found.",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 


    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.fullMark.config(text="")
        self.percentage.config(text="")
        self.var_search.set("")


    def delete(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","search a result first",parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid",parent=self.root)
                else :
                    op=messagebox.askyesno("confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Success","result deleted successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def goback(self):
        self.root.destroy()
        



if __name__== "__main__":
    root=Tk()
    obj=view_class(root)
    root.mainloop()