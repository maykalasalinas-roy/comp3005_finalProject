#This file is for querying the database

import sqlite3

conn = sqlite3.connect("bookstore.db")
c = conn.cursor()

def bookByISBN(isbn):
    '''Gets the isbn and title of a book using the isbn from the database and returns the 
       formatted output for displaying the book'''
    c.execute('''SELECT b.isbn, b.title FROM Book b WHERE b.isbn = ?''', (isbn,))
    r = c.fetchall()

    if(not r):
        return f"isbn '{isbn}' does not exist"

    return printBooks(r)

def bookByTitle(title):
    '''Gets the isbn and title using the title from the database and returns the 
       formatted output for displaying the books'''
    c.execute('''SELECT b.isbn, b.title FROM Book b WHERE title = ?''', (title,))
    r = c.fetchall()

    if(not r):
        return f"Title '{title}' does not exist"

    return printBooks(r)

def bookByAuthor(fname, lname):
    '''Gets the isbn and title using the author from the database and returns the 
       formatted output for displaying the books written by that author'''
    c.execute('''SELECT b.isbn, b.title FROM Book b, wrote w WHERE w.isbn = b.isbn AND w.fname = ? AND w.lname = ?''', (fname, lname,))
    r = c.fetchall()

    if(not r):
        return f"Author '{fname} {lname}' does not exist"

    return printBooks(r)

def bookByPublisher(fname, lname):
    '''Gets the isbn and title using the publisher name from the database and returns the 
       formatted output for displaying the books published by that publisher'''
    c.execute('''SELECT b.isbn, b.title FROM Book b, Publisher p WHERE p.email = b.publisher_email AND p.fname = ? AND p.lname = ?''', (fname, lname,))
    r = c.fetchall()

    if(not r):
        return f"Publisher '{fname} {lname}' does not exist"

    return printBooks(r)

def bookByGenre(genre):
    '''Gets the isbn and title using the genre from the database and returns the 
       formatted output for displaying the books with the genre'''
    c.execute('''SELECT b.isbn, b.title FROM Book b, genre g WHERE b.isbn = g.isbn AND g.genre = ?''', (genre,))
    r = c.fetchall()

    if(not r):
        return f"Genre '{genre}' does not exist"

    return printBooks(r)

def printBooks(books):
    '''Makes a string to display basic information about books'''
    text = "isbn           title"
    for b in books:
        text += f"\n{b[0]}  {b[1]}"

    return text

def viewBook(isbn):
    '''Gets information about a book from the database and returns the string made by printBook'''
    c.execute('''SELECT b.isbn, b.title, b.num_pages, b.sale_price, p.fname, p.lname FROM Book b, Publisher p WHERE b.publisher_email = p.email AND b.isbn = ?''', (isbn,))
    r = c.fetchall()

    c.execute('''SELECT w.fname, w.lname FROM Book b, wrote w WHERE w.isbn = b.isbn AND b.isbn = ?''', (isbn,))
    a = c.fetchall()

    c.execute('''SELECT g.genre FROM Book b, genre g WHERE g.isbn = b.isbn AND b.isbn = ?''', (isbn,))
    g = c.fetchall()

    return printBook(r, a, g)

def printBook(book, a, g):
    '''Makes a string to display detailed information about a book'''
    authors = ""

    for author in a:
        t = author[0] + " " + author[1] + ", "
        authors += t
    padA = len(authors)
    authors = authors[0:padA-2]
    padA = padA - 2

    genres = ""
    for genre in g:
        t = genre[0] + ", "
        genres += t
    genres = genres[0:len(genres)-2]    

    pub = book[0][4] + " " + book[0][5]

    text = "\nisbn | title | num_pages | sale_price | authors | publisher | genres"
    text += f"\n{book[0][0]} | {book[0][1]} | {book[0][2]} | {book[0][3]} | {authors} | {pub}  | {genres}"
    return text

def findUser(email):
    '''Gets information about a registered user if they exist'''
    c.execute('''SELECT email, address, bank_info FROM Registered_user WHERE email = ?''', (email,))
    r = c.fetchone()

    if(r):
        return r
    else:
        return 0

def getTitle(isbn):
    '''Gets the title of a book'''
    c.execute('''SELECT title FROM Book WHERE isbn = ?''', (isbn,))
    r = c.fetchone()
    return r[0]

def getQuantity(isbn):
    '''Gets the quantity of a book'''
    c.execute('''SELECT quantity FROM Book WHERE isbn = ?''', (isbn,))
    r = c.fetchone()
    return r[0]

def getMaxOrderNum():
    '''Gets the highest/most recent order number in the database'''
    c.execute('''SELECT MAX(order_num) FROM book_order''')
    r = c.fetchone()

    if(r[0]):
        return r[0]
    else:
        return 999

def viewOrder(orderNum):
    '''Gets information about an order (tracking, the books and their quantity) and returns a string of the information'''
    c.execute('''SELECT tracking FROM book_order WHERE order_num = ?''', (orderNum,))
    r = c.fetchone()
    
    if(not r):
        return f"Order '{orderNum}' does not exist"

    text = f"Order: {orderNum}, Tracking: {r[0]}\nisbn | quantity\n"

    c.execute('''SELECT isbn, quantity FROM contains WHERE order_num = ?''', (orderNum,))
    r = c.fetchall()

    for b in r:
        text += f"{b[0]} | {b[1]}\n"

    return text

def salesVsExpenses():
    '''Makes a sales vs expenses report using information from the database'''
    c.execute('''SELECT ts.isbn, ts.quantity, ts.sale_price, s.quantity, s.pub_percent FROM Total_sales ts, sells s WHERE ts.isbn = s.isbn''')
    r = c.fetchall()

    totP = 0.0
    totE = 0.0

    text = "isbn \t quantity sold \t sale_price \t total \t quantity bought  pub_percent \t expense \t profit\n"

    for s in r:
        total = s[1] * s[2] # quantity sold * sale_price
        expense = s[3] * (s[2] - (s[2] * (s[4]/100))) # quanty bought from publisher * (sale_price - (sale_price * (pub_percent/100)))
        profit = total - expense

        text += f"{s[0]} \t {s[1]:13} \t {s[2]:10} \t {total:.2f} \t {s[3]:15} \t {s[4]:11} \t {expense:.2f} \t {profit:.2f}\n"
        totP += profit
        totE += expense

    return printSalesVsExpenses(totP, totE, text)

def printSalesVsExpenses(totP, totE, text):
    '''Adds all of the information for the sales vs expenses report'''
    t = f"Total Profit: {totP:.2f}, Total Expenses: {totE:.2f}\n"
    t += text
    return t

def getSalesPerAuthor():
    '''Makes a sales per author report using information from the database'''
    c.execute('''SELECT w.fname, w.lname, ts.quantity FROM Book b, wrote w, Total_sales ts WHERE ts.isbn = b.isbn AND w.isbn = b.isbn GROUP BY w.fname, w.lname''')
    r = c.fetchall()

    text = "author | total books sold\n"
    for s in r:
        text += f"{s[0]} {s[1]} | {s[2]}\n"

    return text

def getSalesPerGenre():
    '''Makes a sales per genre report using information from the database'''
    c.execute('''SELECT g.genre, ts.quantity FROM Book b, genre g, Total_sales ts WHERE ts.isbn = b.isbn AND g.isbn = b.isbn GROUP BY g.genre''')
    r = c.fetchall()

    text = "genre | total books sold\n"
    for s in r:
        text += f"{s[0]} | {s[1]}\n"

    return text

def getSalesPerPublisher():
    '''Makes a sales per publisher report using information from the database'''
    c.execute('''SELECT p.fname, p.lname, ts.quantity FROM Book b, Publisher p, Total_sales ts WHERE ts.isbn = b.isbn AND p.email = b.publisher_email GROUP BY p.fname, p.lname''')
    r = c.fetchall()

    text = "publisher | total books sold\n"
    for s in r:
        text += f"{s[0]} {s[1]} | {s[2]}\n"

    return text

def getAuthors():
    '''Gets all of the author names for the dropdown in the gui'''
    c.execute('''SELECT a.fname, a.lname FROM Author a ORDER BY a.fname, a.lname''')
    r = c.fetchall()
    
    temp = []
    for a in r:
        name = f"{a[0]} {a[1]}"
        temp.append(name)

    return temp

def getPublishers():
    '''Gets all of the publisher names for the dropdown in the gui'''
    c.execute('''SELECT DISTINCT p.email FROM Publisher p ORDER BY p.email''')
    r = c.fetchall()

    temp = []
    for p in r:
        pub = p[0]
        temp.append(pub)

    return temp

def getGenres():
    '''Gets all of the genres for the dropdown in the gui'''
    c.execute('''SELECT DISTINCT g.genre FROM genre g ORDER BY g.genre''')
    r = c.fetchall()

    temp = []
    for g in r:
        genre = g[0]
        temp.append(genre)

    return temp

def getISBN():
    '''Gets all of the isbns for the dropdown in the gui'''
    c.execute('''SELECT DISTINCT isbn FROM Book ORDER BY isbn''')
    r = c.fetchall()

    temp = []
    for b in r:
        isbn = b[0]
        temp.append(isbn)

    return temp