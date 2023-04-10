import sqlite3
def create_db():
    con=sqlite3.connect(database="result.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,amount text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student(rollno INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,admission text,course text,address text)")
    con.commit()


    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,rollno text,name text,course text,marks text,fullMark text,percentage text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS register(id INTEGER PRIMARY KEY AUTOINCREMENT,f_name text,l_name text,contact text,email text,password text)")
    con.commit()


    con.close()


create_db()    