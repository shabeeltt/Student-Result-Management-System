from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class resultC:

    def __init__(self,root):
         self.root=root
         self.root.title("Student Result Management System")
         self.root.geometry("1000x430+80+50")
         self.root.config(bg="lightyellow")
         self.root.focus_force()

         title=Label(self.root,text="Add Student Results",font=("goudy old style",20,"bold"),bg="#EE1019",fg="white").place(x=0,y=15,width=1000,height=35)

         self.var_roll=StringVar()
         self.var_name=StringVar()
         self.var_course=StringVar()
         self.var_markObtained=StringVar()
         self.var_totalMark=StringVar()



         self.roll_list=[]
         self.fetch_rollno()

         lbl_studentSelect=Label(self.root,text="Select Student",font=("goudy old style",18,"bold"),bg="lightyellow").place(x=20,y=70)
         lbl_studentName=Label(self.root,text="Name",font=("goudy old style",18,"bold"),bg="lightyellow").place(x=20,y=120)
         lbl_course=Label(self.root,text="Course",font=("goudy old style",18,"bold"),bg="lightyellow").place(x=20,y=170)
         lbl_markObtained=Label(self.root,text="Mark Obtained",font=("goudy old style",18,"bold"),bg="lightyellow").place(x=20,y=220)
         lbl_totalMark=Label(self.root,text="Total Mark",font=("goudy old style",18,"bold"),bg="lightyellow").place(x=20,y=270)


         self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",18,"bold"),state='readonly',justify=CENTER)
         self.txt_student.place(x=220,y=70,width=150)
         self.txt_student.set("Select")
         self.btn_search= Button(self.root,text="Search",font=("goudy old stle",12,"bold"),bg="#2C4DEA",fg="white",activebackground="lightblue",cursor="hand2",command=self.search)
         self.btn_search.place(x=390,y=70,width=70,height=35)

         self.btn_submit= Button(self.root,text="Submit",font=("goudy old stle",12,),bg="lightgreen",activebackground="yellow",cursor="hand2",command=self.add)
         self.btn_submit.place(x=270,y=330,width=70,height=35)
         self.btn_clear= Button(self.root,text="Clear",font=("goudy old stle",12,),bg="lightgray",activebackground="white",cursor="hand2",command=self.clear)
         self.btn_clear.place(x=360,y=330,width=70,height=35)
         txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18,"bold"),bg="white",state='readonly').place(x=220,y=120,width=240)
         txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",18,"bold"),bg="white",state='readonly').place(x=220,y=170,width=240)
         txt_markObtained=Entry(self.root,textvariable=self.var_markObtained,font=("goudy old style",18,"bold"),bg="white").place(x=220,y=220,width=240)
         txt_totalMark=Entry(self.root,textvariable=self.var_totalMark,font=("goudy old style",18,"bold"),bg="white").place(x=220,y=270,width=240)
        

         self.bg_img=Image.open("images/result.png")
         self.bg_img=self.bg_img.resize((500,300),Image.ANTIALIAS)
         self.bg_img=ImageTk.PhotoImage(self.bg_img)
         self.lbl_img=Label(self.root,image=self.bg_img).place(x=500,y=70,width=450,height=300)


    def fetch_rollno(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            cur.execute("select rollno from student ")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    
    def search(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            cur.execute("select name,course from student where rollno =?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record found.",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  


    def add(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="Select":
                messagebox.showerror("Error"," Select a student.",parent=self.root)
            else:
                cur.execute("select * from result where rollno=? AND course=?",(self.var_roll.get(),self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already uploaded",parent=self.root)
                else :
                    percentage=(int(self.var_markObtained.get())*100)/int(self.var_totalMark.get())
                    cur.execute("insert into result(rollno,name,course,marks,fullMark,percentage) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_markObtained.get(),
                        self.var_totalMark.get(),
                        str(percentage)
                    ))
                    con.commit()
                    messagebox.showinfo("success","Result added successfully.",parent=self.root)
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 


    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_markObtained.set(""),
        self.var_totalMark.set("")


if __name__== "__main__":
    root=Tk()
    obj=resultC(root)
    root.mainloop()
