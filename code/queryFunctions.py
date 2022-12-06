import sqlite3

conn = sqlite3.connect("bookstore.db")
c = conn.cursor()

# Note: 1st search should show like isbn, title and once selected show pages, price, pub, authors, genres
def bookByISBN(isbn):
    c.execute('''SELECT b.isbn, b.title, b.num_pages, b.sale_price, w.fname, w.lname FROM Book b, wrote w WHERE w.isbn = b.isbn AND b.isbn = ?''', (isbn,))
    r = c.fetchall()
    printBooks(r)

def bookByTitle(title):
    c.execute('''SELECT b.isbn, b.title, b.num_pages, b.sale_price FROM Book b WHERE title = ?''', (title,))
    r = c.fetchall()
    printBooks(r)

def bookByAuthor(fname, lname):
    c.execute('''SELECT b.isbn, b.title, b.num_pages, b.sale_price FROM Book b , wrote w WHERE w.isbn = b.isbn AND w.fname = ? AND w.lname = ?''', (fname, lname,))
    r = c.fetchall()
    printBooks(r)

def bookByPublisher(fname, lname):
    c.execute('''SELECT b.isbn, b.title, b.num_pages, b.sale_price FROM Book b , Publisher p WHERE p.email = b.publisher_email AND p.fname = ? AND p.lname = ?''', (fname, lname,))
    r = c.fetchall()
    printBooks(r)

def bookByGenre(genre):
    c.execute('''SELECT b.isbn, b.title, b.num_pages, b.sale_price FROM Book b , genre g WHERE b.isbn = g.isbn AND g.genre = ?''', (genre,))
    r = c.fetchall()
    printBooks(r)

def printBooks(books):
    print(f"isbn           title                                     num_pages  sale_price")
    for b in books:
        print(f"{b[0]}  {b[1]:40}  {b[2]:6}  {b[3]:10}")

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
bookByGenre("Crime")'''