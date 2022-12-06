
-- BOOK QUERIES --

-- Basic views of just isbn and title
-- Query Book by isbn
SELECT b.isbn, b.title FROM Book b WHERE b.isbn = "";

-- Query Book by title
SELECT b.isbn, b.title FROM Book b WHERE b.title = "";

-- Query Book by author first and last name
SELECT b.isbn, b.title FROM Book b , wrote w WHERE w.isbn = b.isbn AND w.fname = "" AND w.lname = "";

-- Query Book by publisher first and last name
SELECT b.isbn, b.title FROM Book b , Publisher p WHERE p.email = b.publisher_email AND p.fname = "" AND p.lname = ""

-- Query Book by genre
SELECT b.isbn, b.title FROM Book b , genre g WHERE b.isbn = g.isbn AND g.genre = ""

-- Queries for viewing a book (all info about them for customer)
-- Get the basic book info
SELECT b.isbn, b.title, b.num_pages, b.sale_price, p.fname, p.lname FROM Book b, Publisher p WHERE b.publisher_email = p.email AND b.isbn = "";
-- Get the author(s)
SELECT w.fname, w.lname FROM Book b, wrote w WHERE w.isbn = b.isbn AND b.isbn = "";
-- Get the genre(s)
SELECT g.genre FROM Book b, genre g WHERE g.isbn = b.isbn AND b.isbn = "";