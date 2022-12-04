import sqlite3

conn = sqlite3.connect("bookstore.db")
c = conn.cursor()

c.execute('''SELECT b.title, b.num_pages, b.sale_price, p.fname, p.lname, w.fname, w.lname FROM Book b, Publisher p, wrote w WHERE (b.isbn = "12-345-678-90" AND b.publisher_email = p.email AND w.isbn = "12-345-678-90")''')
conn.commit()

c.close()
conn.close()