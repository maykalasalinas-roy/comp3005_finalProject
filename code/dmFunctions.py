import sqlite3
import random

conn = sqlite3.connect("bookstore.db")
c = conn.cursor()

def registerUser(email, fname, lname, address, bank_info):
    c.execute('''INSERT INTO Registered_user VALUES(?, ?, ?, ?, ?);''', (email, fname, lname, address, bank_info,))
    conn.commit()

def makeBookOrder(n, user, address, bank_info, books):
    print(n)
    r = random.randint(1, 100)
    if(r % 2 == 0):
        tracking = "warehouse"
    else:
        tracking = "in transit"

    c.execute('''INSERT INTO book_order VALUES(?, ?, ?, ?, ?);''', (n, user, tracking, address, bank_info,))
    conn.commit()

    placeBookOrder(n, books)

def placeBookOrder(n, books):
    for b in books:
        print(f"order num: {n}, isbn: {b[0]}, q: {b[1]}")
        c.execute('''INSERT INTO contains VALUES(?, ?, ?);''', (n, b[0], b[1],))
        conn.commit()

        if(not checkStock(b[0])):
            print("need more books, ordering 10")
            purchaseBook(b[0])
        
def purchaseBook(isbn):
    c.execute('''UPDATE sells SET quantity = quantity + 10 WHERE isbn = ?''', (isbn,))
    conn.commit()

    c.execute('''UPDATE Book SET quantity = quantity + 10 WHERE isbn = ?''', (isbn,))
    conn.commit()

def orderBook(isbn, quantity):
    print(f"ordering {quantity} of book with isbn {isbn}")
    c.execute('''UPDATE sells SET quantity = quantity + ? WHERE isbn = ?''', (quantity, isbn,))
    conn.commit()

    c.execute('''UPDATE Book SET quantity = quantity + ? WHERE isbn = ?''', (quantity, isbn,))
    conn.commit()

def checkStock(isbn):
    c.execute('''SELECT quantity FROM Book WHERE isbn = ?''', (isbn,))
    r = c.fetchone()

    if(r[0] < 10):
        return False
    else:
        return True

def newBook(isbn, pEmail, title, numP, price, pubP, fn, ln, genre):
    c.execute('''INSERT INTO Book VALUES(?, ?, ?, ?, ?, ?);''', (isbn, pEmail, title, numP, 10, price,))
    conn.commit()

    c.execute('''INSERT INTO wrote VALUES(?, ?, ?);''', (isbn, fn, ln,))
    conn.commit()

    c.execute('''INSERT INTO genre VALUES(?, ?);''', (isbn, genre,))
    conn.commit()

    c.execute('''INSERT INTO sells VALUES(?, ?, ?);''', (isbn, 10, pubP,))
    conn.commit()

    c.execute('''INSERT INTO Total_sales VALUES(?, ?, ?);''', (isbn, 0, price,))
    conn.commit()

    

'''
n = 1000
cart = [("12-345-678-11", 3), ("12-345-678-56", 6), ("12-345-678-34", 10)]

makeBookOrder(n, "abc@test.ca", "street", "123456789123", cart)'''