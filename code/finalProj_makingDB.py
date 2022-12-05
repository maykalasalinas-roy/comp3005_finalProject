import sqlite3

conn = sqlite3.connect("bookstore.db")
c = conn.cursor()
c.execute('''DROP TABLE Book''')
c.execute('''DROP TABLE genre''')
c.execute('''DROP TABLE Publisher''')
c.execute('''DROP TABLE phones''')
c.execute('''DROP TABLE Author''')
c.execute('''DROP TABLE wrote''')
c.execute('''DROP TABLE registered_user''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS Publisher (
    email VARCHAR(20) PRIMARY KEY,
	fname VARCHAR(15) NOT NULL,
	lname VARCHAR(15) NOT NULL,
	address VARCHAR(30),
	bank_info VARCHAR(12) NOT NULL UNIQUE)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS phones (
	publisher_email VARCHAR(20),
	phone CHAR(9),
	PRIMARY KEY(publisher_email, phone),
	FOREIGN KEY (publisher_email) REFERENCES Publisher (email))''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS Author (
	fname VARCHAR(15),
	lname VARCHAR(15),
	PRIMARY KEY (fname, lname))''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS Book (
	isbn CHAR(17) PRIMARY KEY,
	publisher_email VARCHAR(20) NOT NULL,
	title VARCHAR(40) NOT NULL,
	num_pages NUMERIC(4, 0) NOT NULL,
	quantity NUMERIC(10, 0) NOT NULL,
	sale_price NUMERIC(5, 2) NOT NULL,
	pub_percent NUMERIC(4, 2) NOT NULL,
	FOREIGN KEY (publisher_email) REFERENCES Publisher (email))''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS genre (
	isbn CHAR(17),
	genre VARCHAR(15),
	PRIMARY KEY (isbn, genre),
	FOREIGN KEY (isbn) REFERENCES Book (isbn))''')
conn.commit()



c.execute('''CREATE TABLE IF NOT EXISTS sells (
	isbn CHAR(17),
	date Date NOT NULL,
	quantity NUMERIC(2, 0) NOT NULL,
	PRIMARY KEY (isbn),
	FOREIGN KEY (isbn) REFERENCES Book (isbn))''')
conn.commit()


c.execute('''CREATE TABLE IF NOT EXISTS wrote (
	isbn CHAR(17),
	fname VARCHAR(15),
	lname VARCHAR(15),
	PRIMARY KEY (isbn, fname, lname),
	FOREIGN KEY (isbn) REFERENCES Book (isbn),
	FOREIGN KEY (fname, lname) REFERENCES Author (fname, lname))''')
conn.commit()


c.execute('''CREATE TABLE IF NOT EXISTS Registered_user (
	email VARCHAR(20) PRIMARY KEY,
    fname VARCHAR(15),
    lname VARCHAR(15),
    address VARCHAR(30) NOT NULL,
    bank_info VARCHAR(12) NOT NULL UNIQUE)''')
conn.commit()


c.execute('''CREATE TABLE IF NOT EXISTS book_order (
	order_num NUMERIC(4,0) PRIMARY KEY,
    user_email VARCHAR(15),
    tracking VARCHAR(10),
    date Date NOT NULL)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS contains (
	order_num NUMERIC(4, 0),
    isbn CHAR(17),
    quantity NUMERIC(2, 0) NOT NULL,
    PRIMARY KEY (order_num, isbn),
    FOREIGN KEY (order_num) REFERENCES Book (isbn))''')
conn.commit()


c.execute('''CREATE TABLE IF NOT EXISTS Total_sales (
	isbn CHAR(17),
	date Date NOT NULL,
	quantity NUMERIC(2, 0) NOT NULL,
	PRIMARY KEY (isbn),
	FOREIGN KEY (isbn) REFERENCES Book (isbn))''')
conn.commit()

c.close()
conn.close()
