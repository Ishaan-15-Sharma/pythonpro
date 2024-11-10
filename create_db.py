import sqlite3 
def create_db():
    con=sqlite3.connect(database=r'ims.db') #r here represents path else we have to write 'file name'/folder name'.db and .db is an in built extension
    cur=con.cursor()
    cur.execute("CREATE Table IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()

    cur.execute("CREATE Table IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    con.commit()

    cur.execute("CREATE Table IF NOT EXISTS category(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()




create_db()
