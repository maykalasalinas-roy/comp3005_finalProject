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

---------------------------------------------

-- Queries for viewing a book (all info about them for customer)
-- Get the basic book info
SELECT b.isbn, b.title, b.num_pages, b.sale_price, p.fname, p.lname FROM Book b, Publisher p WHERE b.publisher_email = p.email AND b.isbn = "";
-- Get the author(s)
SELECT w.fname, w.lname FROM Book b, wrote w WHERE w.isbn = b.isbn AND b.isbn = "";
-- Get the genre(s)
SELECT g.genre FROM Book b, genre g WHERE g.isbn = b.isbn AND b.isbn = "";

-----------------------------------------------

-- Query to get user information to autopopulate fields after logging in
SELECT email, address, bank_info FROM Registered_user WHERE email = ?

-----------------------------------------------

-- Used for displaying the cart (cart stores isbn and quantity)
-- Get the title
SELECT title FROM Book WHERE isbn = ?

-----------------------------------------------

-- Little helper queries
-- Used for populating the spinbox(to select quantity to add to cart)
SELECT quantity FROM Book WHERE isbn = ?

-- Gets the largest order number so I can assign the next one
SELECT MAX(order_num) FROM book_order

-----------------------------------------------

-- For displaying an order from an isbn
-- Get tracking info
SELECT tracking FROM book_order WHERE order_num = ?
-- Get isbn and quantity
SELECT isbn, quantity FROM contains WHERE order_num = ?

-----------------------------------------------

-- Displaying reports
-- For getting sales vs expenses
SELECT ts.isbn, ts.quantity, ts.sale_price, s.quantity, s.pub_percent FROM Total_sales ts, sells s WHERE ts.isbn = s.isbn
-- Sales per author
SELECT w.fname, w.lname, ts.quantity FROM Book b, wrote w, Total_sales ts WHERE ts.isbn = b.isbn AND w.isbn = b.isbn GROUP BY w.fname, w.lname
-- Sales per genre
SELECT g.genre, ts.quantity FROM Book b, genre g, Total_sales ts WHERE ts.isbn = b.isbn AND g.isbn = b.isbn GROUP BY g.genre
-- Sales per publisher
SELECT p.fname, p.lname, ts.quantity FROM Book b, Publisher p, Total_sales ts WHERE ts.isbn = b.isbn AND p.email = b.publisher_email GROUP BY p.fname, p.lname

-----------------------------------------------

-- Little helper queries for populating dropdowns
-- Author names
SELECT a.fname, a.lname FROM Author a ORDER BY a.fname, a.lname
-- Publisher emails
SELECT DISTINCT p.email FROM Publisher p ORDER BY p.email
-- Genres
SELECT DISTINCT g.genre FROM genre g ORDER BY g.genre
-- ISBNs
SELECT DISTINCT isbn FROM Book ORDER BY isbn

