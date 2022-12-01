CREATE TABLE IF NOT EXISTS Publisher (
	fname VARCHAR(15) NOT NULL,
	lname VARCHAR(15) NOT NULL,
	email VARCHAR(20) PRIMARY KEY,
	address VARCHAR(30),
	bank_info VARCHAR(12) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS phones (
	publisher_email VARCHAR(20),
	phone CHAR(9),
	PRIMARY KEY(publisher_email, phone),
	FOREIGN KEY (publisher_email) REFERENCES Publisher (email)
);

CREATE TABLE IF NOT EXISTS Author (
	fname VARCHAR(15),
	lname VARCHAR(15),
	PRIMARY KEY (fname, lname)
);

CREATE TABLE IF NOT EXISTS Book (
	isbn CHAR(17) PRIMARY KEY, -- isbn are 13 digits but they have 4 hyphens
	publisher_email VARCHAR(20) NOT NULL,
	title VARCHAR(15) NOT NULL,
	num_pages NUMERIC(4, 0) NOT NULL,
	quantity NUMERIC(10, 0) NOT NULL,
	pub_percent NUMERIC(4, 2) NOT NULL,
	FOREIGN KEY (publisher_email) REFERENCES Publisher (email)
);
