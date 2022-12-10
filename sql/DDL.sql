
-- Publisher table
CREATE TABLE IF NOT EXISTS Publisher (
    email VARCHAR(20) PRIMARY KEY,
	fname VARCHAR(15) NOT NULL,
	lname VARCHAR(15) NOT NULL,
	address VARCHAR(30),
	bank_info VARCHAR(12) NOT NULL UNIQUE
);

-- Phone numbers of publishers
CREATE TABLE IF NOT EXISTS phones (
	publisher_email VARCHAR(20),
	phone CHAR(9),
	PRIMARY KEY(publisher_email, phone),
	FOREIGN KEY (publisher_email) REFERENCES Publisher (email)
);

-- Author table
CREATE TABLE IF NOT EXISTS Author (
	fname VARCHAR(15),
	lname VARCHAR(15),
	PRIMARY KEY (fname, lname)
);

-- Book table
CREATE TABLE IF NOT EXISTS Book (
	isbn CHAR(17) PRIMARY KEY, -- isbn are 13 digits but they have 4 hyphens
	publisher_email VARCHAR(20) NOT NULL,
	title VARCHAR(40) NOT NULL,
	num_pages NUMERIC(4, 0) NOT NULL,
	quantity NUMERIC(10, 0) NOT NULL,
	sale_price NUMERIC(5, 2) NOT NULL,
	FOREIGN KEY (publisher_email) REFERENCES Publisher (email)
);

-- genres for books
CREATE TABLE IF NOT EXISTS genre (
	isbn CHAR(17),
	genre VARCHAR(15),
	PRIMARY KEY (isbn, genre),
	FOREIGN KEY (isbn) REFERENCES Book (isbn)
);

-- Stores the books sold by the publishers to the bookstore
CREATE TABLE IF NOT EXISTS sells (
	isbn CHAR(17),
	quantity NUMERIC(2, 0) NOT NULL,
	pub_percent NUMERIC(4, 2) NOT NULL,
	PRIMARY KEY (isbn),
	FOREIGN KEY (isbn) REFERENCES Book (isbn)
);

-- Authors and books they've written
CREATE TABLE IF NOT EXISTS wrote (
	isbn CHAR(17),
	fname VARCHAR(15),
	lname VARCHAR(15),
	PRIMARY KEY (isbn, fname, lname),
	FOREIGN KEY (isbn) REFERENCES Book (isbn),
	FOREIGN KEY (fname, lname) REFERENCES Author (fname, lname)
);

-- Registered_user table
CREATE TABLE IF NOT EXISTS Registered_user (
	email VARCHAR(20) PRIMARY KEY,
    fname VARCHAR(15),
    lname VARCHAR(15),
    address VARCHAR(30) NOT NULL,
    bank_info VARCHAR(12) NOT NULL UNIQUE
);

-- Book order
CREATE TABLE IF NOT EXISTS book_order (
	order_num NUMERIC(4,0) PRIMARY KEY,
    user_email VARCHAR(15),
    tracking VARCHAR(10), -- Going to be like "warehouse" or "in transit" so it's 9 to 10 characters
	address VARCHAR(30) NOT NULL,
	bank_info VARCHAR(12) NOT NULL
);

-- Books that are part of orders
CREATE TABLE IF NOT EXISTS contains (
	order_num NUMERIC(4, 0),
    isbn CHAR(17),
    quantity NUMERIC(2, 0) NOT NULL,
    PRIMARY KEY (order_num, isbn),
    FOREIGN KEY (order_num) REFERENCES Book (isbn)
);

-- total sales of books sold by the bookstore
CREATE TABLE IF NOT EXISTS Total_sales (
	isbn CHAR(17),
	quantity NUMERIC(2, 0) NOT NULL,
	sale_price NUMERIC(5, 2) NOT NULL,
	PRIMARY KEY (isbn),
	FOREIGN KEY (isbn) REFERENCES Book (isbn)
);