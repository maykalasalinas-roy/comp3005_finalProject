
-- BOOK QUERIES
-- Query Book by isbn
SELECT b.isbn, b.title, b.num_pages, b.sale_price, w.fname, w.lname FROM Book b, wrote w WHERE w.isbn = b.isbn AND b.isbn = "";

-- Query Book by title
SELECT b.isbn, b.title, b.num_pages, b.sale_price FROM Book b WHERE title = "";

-- Query Book by author first and last name
SELECT b.isbn, b.title, b.num_pages, b.sale_price FROM Book b , wrote w WHERE w.isbn = b.isbn AND w.fname = "" AND w.lname = "";

-- Query Book by publisher first and last name
SELECT b.isbn, b.title, b.num_pages, b.sale_price FROM Book b , Publisher p WHERE p.email = b.publisher_email AND p.fname = "" AND p.lname = ""

-- Query Book by genre
SELECT b.isbn, b.title, b.num_pages, b.sale_price FROM Book b , genre g WHERE b.isbn = g.isbn AND g.genre = ""