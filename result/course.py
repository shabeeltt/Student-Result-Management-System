from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class courseC:

    def __init__(self,root):
         self.root=root
         self.root.title("Student Result Management System")
         self.root.geometry("1200x600+80+50")
         self.root.config(bg="#F9ec87")
         self.root.focus_force()

         title=Label(self.root,text="Course Catalog",font=("goudy old style",20,"bold"),bg="#123456",fg="#DADBDD").place(x=00,y=15,width=1200,height=35)

         self.var_course=StringVar()
         self.var_duration=StringVar()
         self.var_amount=StringVar()
        
         lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=12,y=70)
         lbl_duration=Label(self.root,text="Duration",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=12,y=120)
         lbl_amount=Label(self.root,text="Amount",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=12,y=170)


         self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",18,"bold"),bg="white")
         self.txt_courseName.place(x=150,y=70,width=230)
         txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",18,"bold"),bg="white").place(x=150,y=120,width=230)
         txt_amount=Entry(self.root,textvariable=self.var_amount,font=("goudy old style",18,"bold"),bg="white").place(x=150,y=170,width=230)
         
         
         
         self.btn_save= Button(self.root,text="Save",font=("goudy old stle",15,"bold"),bg="#790FB7",fg="white",cursor="hand2",command=self.add)
         self.btn_save.place(x=100,y=450,width=110,height=40)
         self.btn_update= Button(self.root,text="Update",font=("goudy old stle",15,"bold"),bg="#790FB7",fg="white",cursor="hand2",command=self.update)
         self.btn_update.place(x=220,y=450,width=110,height=40)
         self.btn_delete= Button(self.root,text="Delete",font=("goudy old stle",15,"bold"),bg="#790FB7",fg="white",cursor="hand2",command=self.delete)
         self.btn_delete.place(x=340,y=450,width=110,height=40)
         self.btn_clear= Button(self.root,text="Clear",font=("goudy old stle",15,"bold"),bg="#Ce3232",fg="white",cursor="hand2",command=self.clear)
         self.btn_clear.place(x=420,y=70,width=110,height=30)



         self.var_search=StringVar()
         lbl_search=Label(self.root,text="Search for course",font=("goudy old style",18,"bold"),bg="#F9ec87").place(x=670,y=70)
         txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",18,"bold"),bg="white").place(x=845,y=70,width=180)
         self.btn_search= Button(self.root,text="Search",font=("goudy old stle",12,"bold"),bg="#1dc71d",fg="white",cursor="hand2",command=self.search)
         self.btn_search.place(x=1040,y=70,width=65,height=28)
         self.btn_clear_search= Button(self.root,text="Clear",font=("goudy old stle",12,"bold"),bg="#Ce3232",fg="white",cursor="hand2",command=self.search_clear)
         self.btn_clear_search.place(x=1110,y=70,width=65,height=28)


         self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
         self.C_Frame.place(x=670,y=130,width=500,height=340)
         
         scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
         scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
         self.courseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","amount"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
         
         scrolly.pack(side=RIGHT,fill=Y)
         scrollx.pack(side=BOTTOM,fill=X)
         scrollx.config(command=self.courseTable.xview)
         scrolly.config(command=self.courseTable.yview)

         self.courseTable.heading("cid",text="Course id")
         self.courseTable.heading("name",text="Name")
         self.courseTable.heading("duration",text="Duration")
         self.courseTable.heading("amount",text="Amount")
         self.courseTable["show"]='headings'
         self.courseTable.column("cid",width=50)
         self.courseTable.column("name",width=100)
         self.courseTable.column("duration",width=100)
         self.courseTable.column("amount",width=100)
         self.courseTable.pack(fill=BOTH,expand=1)
         self.courseTable.bind("<ButtonRelease-1>",self.get_data)
         self.show()


    def search_clear(self):
        self.show()
        self.var_search.set("")
    
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_amount.set("")
        self.txt_courseName.config(state=NORMAL)

    def delete(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Course is not selected",parent=self.root)
                else :
                    op=messagebox.askyesno("confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Success","course deleted successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    
    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        self.txt_courseName
        r=self.courseTable.focus()
        content=self.courseTable.item(r)
        row=content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_amount.set(row[3])


    def add(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Name cannot be null",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name already exist",parent=self.root)
                else :
                    cur.execute("insert into course(name,duration,amount) values(?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_amount.get()
                    ))
                    con.commit()
                    messagebox.showinfo("success","Course added successfully.",parent=self.root)
                    self.show()
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def update(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Name cannot be null",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Select course from the list.",parent=self.root)
                else :
                    cur.execute("update course set duration=?,amount=? where name=?",(
                        self.var_duration.get(),
                        self.var_amount.get(),
                        self.var_course.get(),
                        
                    ))
                    con.commit()
                    messagebox.showinfo("success","Course updated successfully.",parent=self.root)
                    self.show()

                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def show(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course ")
            rows=cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    

    def search(self):
        con=sqlite3.connect(database="result.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")   



         
if __name__== "__main__":
    root=Tk()
    obj=courseC(root)
    root.mainloop()
