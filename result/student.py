from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class studentC:

    def __init__(self,root):
         self.root=root
         self.root.title("Student Result Management System")
         self.root.geometry("1200x600+80+50")
         self.root.config(bg="#F9ec87")
         self.root.focus_force()

         title=Label(self.root,text="Student Details",font=("goudy old style",20,"bold"),bg="#123456",fg="#DADBDD").place(x=00,y=15,width=1200,height=35)

         self.var_roll=StringVar()
         self.var_name=StringVar()
         self.var_email=StringVar()
         self.var_gender=StringVar()
         self.var_dob=StringVar()
         self.var_contact=StringVar()
         self.var_course=StringVar()
         self.var_a_date=StringVar()

        
         lbl_rollNo=Label(self.root,text="Roll No",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=12,y=70)
         lbl_Name=Label(self.root,text="Name",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=12,y=120)
         lbl_Email=Label(self.root,text="Email",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=12,y=170)
         lbl_gender=Label(self.root,text="Gender",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=12,y=220)
         lbl_address=Label(self.root,text="Address",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=12,y=270)


         self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",18,"bold"),bg="white")
         self.txt_roll.place(x=100,y=70,width=200)
         txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18,"bold"),bg="white").place(x=100,y=120,width=200)
         txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",18,"bold"),bg="white").place(x=100,y=170,width=200)
         self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("goudy old style",18,"bold"),state='readonly',justify=CENTER)
         self.txt_gender.place(x=100,y=220,width=200)
         self.txt_gender.current(0)


         lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=310,y=70)
         lbl_contact=Label(self.root,text="Contact",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=310,y=120)
         lbl_admission_no=Label(self.root,text="Admission No",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=310,y=170)
         lbl_course=Label(self.root,text="Course",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=310,y=220)

         self.course_list=[]

         self.fetch_course()
         self.txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",18,"bold"),bg="white")
         self.txt_dob.place(x=400,y=70,width=200)
         txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",18,"bold"),bg="white").place(x=400,y=120,width=200)
         txt_admission=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",18,"bold"),bg="white").place(x=465,y=170,width=135)
         self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",18,"bold"),state='readonly',justify=CENTER)
         self.txt_course.place(x=400,y=220,width=200)
         self.txt_course.set("Select")
         






         self.txt_address=Text(self.root,font=("goudy old style",18,"bold"),bg="white")
         self.txt_address.place(x=100,y=280,width=500,height=130)
         
         
         self.btn_save= Button(self.root,text="Save",font=("goudy old stle",15,"bold"),bg="#790FB7",fg="white",cursor="hand2",command=self.add)
         self.btn_save.place(x=100,y=500,width=110,height=40)
         self.btn_update= Button(self.root,text="Update",font=("goudy old stle",15,"bold"),bg="#790FB7",fg="white",cursor="hand2",command=self.update)
         self.btn_update.place(x=220,y=500,width=110,height=40)
         self.btn_delete= Button(self.root,text="Delete",font=("goudy old stle",15,"bold"),bg="#790FB7",fg="white",cursor="hand2",command=self.delete)
         self.btn_delete.place(x=340,y=500,width=110,height=40)
         self.btn_clear= Button(self.root,text="Clear",font=("goudy old stle",15,"bold"),bg="#Ce3232",fg="white",cursor="hand2",command=self.clear)
         self.btn_clear.place(x=460,y=500,width=110,height=40)



         self.var_search=StringVar()
         lbl_search_roll=Label(self.root,text="Search Roll No",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=670,y=70)
         txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",18,"bold"),bg="white").place(x=845,y=70,width=180)
         self.btn_search= Button(self.root,text="Search",font=("goudy old stle",12,"bold"),bg="#1dc71d",fg="white",cursor="hand2",command=self.search)
         self.btn_search.place(x=1040,y=70,width=65,height=28)
         self.btn_clear_search= Button(self.root,text="Clear",font=("goudy old stle",12,"bold"),bg="#Ce3232",fg="white",cursor="hand2",command=self.search_clear)
         self.btn_clear_search.place(x=1110,y=70,width=65,height=28)


         self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
         self.C_Frame.place(x=670,y=130,width=500,height=405)
         
         scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
         scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
         self.courseTable=ttk.Treeview(self.C_Frame,columns=("rollno","name","email","gender","dob","contact","admission","course","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
         
         scrolly.pack(side=RIGHT,fill=Y)
         scrollx.pack(side=BOTTOM,fill=X)
         scrollx.config(command=self.courseTable.xview)
         scrolly.config(command=self.courseTable.yview)

         self.courseTable.heading("rollno",text="Roll No")
         self.courseTable.heading("name",text="Name")
         self.courseTable.heading("email",text="Email")
         self.courseTable.heading("gender",text="Gender")
         self.courseTable.heading("dob",text="D.O.B")
         self.courseTable.heading("contact",text="Contact")
         self.courseTable.heading("admission",text="Admission no")
         self.courseTable.heading("course",text="Course")
         self.courseTable.heading("address",text="Address")
         self.courseTable["show"]='headings'
         self.courseTable.column("rollno",width=100)
         self.courseTable.column("name",width=100)
         self.courseTable.column("email",width=100)
         self.courseTable.column("gender",width=100)
         self.courseTable.column("dob",width=100)
         self.courseTable.column("contact",width=100)
         self.courseTable.column("admission",width=100)
         self.courseTable.column("course",width=100)
         self.courseTable.column("address",width=100)
         self.courseTable.pack(fill=BOTH,expand=1)
         self.courseTable.bind("<ButtonRelease-1>",self.get_data)
         self.show()
         


    def search_clear(self):
        self.show()
        self.var_search.set("")
    
    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),               
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set("Select"),
        self.txt_address.delete("1.0",END)
        self.txt_roll.config(state=NORMAL)

    def delete(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:
                cur.execute("select * from student where rollno=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Student is not selected",parent=self.root)
                else :
                    op=messagebox.askyesno("confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where rollno=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Success","student deleted successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    
    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        r=self.courseTable.focus()
        content=self.courseTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),               
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[8])
        


    def add(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required.",parent=self.root)
            else:
                cur.execute("select * from student where rollno=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Roll No. already exist.",parent=self.root)
                else :
                    cur.execute("insert into student(rollno,name,email,gender,dob,contact,admission,course,address) values(?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("success","Student added successfully.",parent=self.root)
                    self.show()
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def update(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. cannot be null",parent=self.root)
            else:
                cur.execute("select * from student where rollno=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Select student from the list.",parent=self.root)
                else :
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,address=? where rollno=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.txt_address.get("1.0",END),
                        self.var_roll.get()
                        
                    ))
                    con.commit()
                    messagebox.showinfo("success","Student updated successfully.",parent=self.root)
                    self.show()

                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def show(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student ")
            rows=cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def fetch_course(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course ")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    

    def search(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student where rollno =?",(self.var_search.get(),))
            row=cur.fetchone()
            if row != None:
                self.courseTable.delete(*self.courseTable.get_children())
                self.courseTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found.")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



         
if __name__== "__main__":
    root=Tk()
    obj=studentC(root)
    root.mainloop()
