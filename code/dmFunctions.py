#This file is for manipulating the database

import sqlite3
import random

conn = sqlite3.connect("bookstore.db")
c = conn.cursor()

def registerUser(email, fname, lname, address, bank_info):
    '''Adds a new row to the Registered_user table'''
    c.execute('''INSERT INTO Registered_user VALUES(?, ?, ?, ?, ?);''', (email, fname, lname, address, bank_info,))
    conn.commit()

def makeBookOrder(n, user, address, bank_info, books):
    '''Adds a new book order to the book_order table'''
    r = random.randint(1, 100)
    if(r % 2 == 0): # randomly pick if the tracking
        tracking = "warehouse"
    else:
        tracking = "in transit"

    c.execute('''INSERT INTO book_order VALUES(?, ?, ?, ?, ?);''', (n, user, tracking, address, bank_info,))
    conn.commit()

    # add to contains
    placeBookOrder(n, books)

def placeBookOrder(n, books):
    '''Adds the books in an order to the contains table'''
    for b in books:
        c.execute('''INSERT INTO contains VALUES(?, ?, ?);''', (n, b[0], b[1],))
        conn.commit()

        if(not checkStock(b[0])):
            print("need more books, ordering 10")
            purchaseBook(b[0])
        
def purchaseBook(isbn):
    '''Orders 10 more books from the publisher'''
    c.execute('''UPDATE sells SET quantity = quantity + 10 WHERE isbn = ?''', (isbn,)) 
    conn.commit()

    c.execute('''UPDATE Book SET quantity = quantity + 10 WHERE isbn = ?''', (isbn,))
    conn.commit()

def orderBook(isbn, quantity):
    '''Orders a specified amount of a book from the publisher'''
    if(checkISBN(isbn)):
        c.execute('''UPDATE sells SET quantity = quantity + ? WHERE isbn = ?''', (quantity, isbn,))
        conn.commit()

        c.execute('''UPDATE Book SET quantity = quantity + ? WHERE isbn = ?''', (quantity, isbn,))
        conn.commit()

        return f"Ordered {quantity} of book with isbn {isbn}"
    else:
        return f"Book with isbn {isbn} does not exist, no order placed."

def checkStock(isbn):
    '''Checks if a book's quantity is greater than 10'''
    c.execute('''SELECT quantity FROM Book WHERE isbn = ?''', (isbn,))
    r = c.fetchone()

    if(r[0] < 10):
        return False
    else:
        return True

def newBook(isbn, pEmail, title, numP, price, pubP, fn, ln, genre):
    '''Adds a new book to the database and its relationships'''
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

def deleteBook(isbn):
    '''Deletes specified book if it exists and creates a string for the output.
       The Total_sales is updated in a trigger when contains is deleted'''
    if(checkISBN(isbn)):
        text = f"Book with isbn: {isbn} deleted and any orders refunded.\n"
        c.execute('''DELETE FROM Book WHERE isbn = ?;''', (isbn,))
        conn.commit()

        (fr, pr) = deleteEmptyOrders(isbn)

        c.execute('''DELETE FROM contains WHERE isbn = ?;''', (isbn,))
        conn.commit()

        text = text + fr + pr

        return text
    else:
        return f"Book with isbn: {isbn} does not exist, no deletes."

def deleteEmptyOrders(isbn):
    '''When a book is deleted, refund affected orders and deletes orders if they are empty(only had the book 
       that is being deleted)'''
    fullRefund = "Fully refunded Orders:\n"
    partialRefund = "Partially refunded Orders:\n"
    c.execute('''SELECT order_num FROM contains WHERE isbn = ?''', (isbn,))
    orders = c.fetchall()

    for o in orders:
        c.execute('''SELECT COUNT(isbn) FROM contains WHERE order_num = ?''', (o[0],))
        r = c.fetchone()

        if(r[0] == 1):
            c.execute('''DELETE FROM book_order WHERE order_num = ?;''', (o[0],))
            conn.commit()
            fullRefund += f"{o[0]}\n"
        else:
            partialRefund += f"{o[0]}\n"

    return (fullRefund, partialRefund)

def checkISBN(isbn):
    '''Checks if an isbn exists in the database'''
    c.execute('''SELECT 1 FROM Book WHERE isbn = ?''', (isbn,))
    r = c.fetchone()

    if(r):
        return r[0]
    else:
        return 0