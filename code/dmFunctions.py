import sqlite3

conn = sqlite3.connect("bookstore.db")
c = conn.cursor()

def registerUser(email, fname, lname, address, bank_info):
    c.execute('''INSERT INTO Registered_user VALUES(?, ?, ?, ?, ?);''', (email, fname, lname, address, bank_info,))
    conn.commit()

