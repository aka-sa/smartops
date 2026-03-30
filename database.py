
import sqlite3
conn=sqlite3.connect("smartops.db",check_same_thread=False)
c=conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY,amount REAL,category TEXT)")
conn.commit()

def add_expense(a,cg):
    c.execute("INSERT INTO expenses(amount,category) VALUES(?,?)",(a,cg))
    conn.commit()

def get_all():
    c.execute("SELECT amount FROM expenses")
    return [x[0] for x in c.fetchall()]
