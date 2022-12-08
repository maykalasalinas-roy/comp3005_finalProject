import sqlite3
import random

conn = sqlite3.connect("bookstore.db")
c = conn.cursor()

def registerUser(email, fname, lname, address, bank_info):
    c.execute('''INSERT INTO Registered_user VALUES(?, ?, ?, ?, ?);''', (email, fname, lname, address, bank_info,))
    conn.commit()

def makeBookOrder(n, user, address, bank_info, books):
    r = random.randint(1, 100)
    if(r % 2 == 0):
        tracking = "warehouse"
    else:
        tracking = "in transit"

    r = random.randint(1, 12)
    date = f"2022-{r}-01"

    c.execute('''INSERT INTO book_order VALUES(?, ?, ?, ?, ?, ?);''', (n, user, tracking, date, address, bank_info,))
    conn.commit()

    placeBookOrder(n, books)

def placeBookOrder(n, books):
    for b in books:
        c.execute('''INSERT INTO contains VALUES(?, ?, ?);''', (n, b[0], b[1],))
        conn.commit()


def sellBook(isbn):
    print("if book in the total_sales then updaate quantity, if not then add")
    print("reduce quantity in the book table") # made trigger

'''
n = 1000
cart = [("12-345-678-11", 3), ("12-345-678-56", 6), ("12-345-678-34", 10)]

makeBookOrder(n, "abc@test.ca", "street", "123456789123", cart)'''