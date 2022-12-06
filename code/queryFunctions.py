import sqlite3

conn = sqlite3.connect("bookstore.db")
c = conn.cursor()

def bookByISBN(isbn):
    c.execute('''SELECT b.isbn, b.title FROM Book b WHERE b.isbn = ?''', (isbn,))
    r = c.fetchall()
    return printBooks(r)

def bookByTitle(title):
    c.execute('''SELECT b.isbn, b.title FROM Book b WHERE title = ?''', (title,))
    r = c.fetchall()
    return printBooks(r)

def bookByAuthor(fname, lname):
    c.execute('''SELECT b.isbn, b.title FROM Book b, wrote w WHERE w.isbn = b.isbn AND w.fname = ? AND w.lname = ?''', (fname, lname,))
    r = c.fetchall()
    return printBooks(r)

def bookByPublisher(fname, lname):
    c.execute('''SELECT b.isbn, b.title FROM Book b, Publisher p WHERE p.email = b.publisher_email AND p.fname = ? AND p.lname = ?''', (fname, lname,))
    r = c.fetchall()
    return printBooks(r)

def bookByGenre(genre):
    c.execute('''SELECT b.isbn, b.title FROM Book b, genre g WHERE b.isbn = g.isbn AND g.genre = ?''', (genre,))
    r = c.fetchall()

    return printBooks(r)

def printBooks(books):
    text = "isbn           title"
    for b in books:
        text += f"\n{b[0]}  {b[1]}"

    return text

def viewBook(isbn):
    c.execute('''SELECT b.isbn, b.title, b.num_pages, b.sale_price, p.fname, p.lname FROM Book b, Publisher p WHERE b.publisher_email = p.email AND b.isbn = ?''', (isbn,))
    r = c.fetchall()

    c.execute('''SELECT w.fname, w.lname FROM Book b, wrote w WHERE w.isbn = b.isbn AND b.isbn = ?''', (isbn,))
    a = c.fetchall()

    c.execute('''SELECT g.genre FROM Book b, genre g WHERE g.isbn = b.isbn AND b.isbn = ?''', (isbn,))
    g = c.fetchall()

    return printBook(r, a, g)

def printBook(book, a, g):
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

    text = "isbn | title | num_pages | sale_price | authors | publisher | genres"
    text += f"\n{book[0][0]} | {book[0][1]} | {book[0][2]} | {book[0][3]} | {authors} | {pub}  | {genres}"
    return text

def findUser(email):
    c.execute('''SELECT 1 FROM Registered_user WHERE email = ?''', (email,))
    r = c.fetchone()
    return r[0]

'''
print("\nQuery using isbn:")
bookByISBN("12-345-678-17")

print("\nQuery using title:")
bookByTitle("Great Escape, The")

print("\nQuery using author:")
bookByAuthor("Anjela", "Abramski")

print("\nQuery using publisher:")
bookByPublisher("Fran", "Oglesbee")

print("\nQuery using genre:")
bookByGenre("Crime")

viewBook("12-345-678-18")
viewBook("12-345-678-75")
viewBook("12-345-678-56")

findUser("cpeartree0@wisc.edu")'''