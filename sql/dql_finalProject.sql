
-- Searching by isbn, query to get the book info, publisher info, authors
SELECT b.title, b.num_pages, b.sale_price, p.fname, p.lname, w.fname, w.lname FROM Book b, Publisher p, wrote w WHERE (b.isbn = "12-345-678-90" AND b.publisher_email = p.email AND w.isbn = "12-345-678-90");

