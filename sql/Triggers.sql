-- Trigger for when an order is made 
-- When I make an order, I do an insertion to book_order and then contains
-- This trigger is for when books are being added to contains, it removes them 
-- from the book's quantity/stock
-- This also increases the total sales for the book
CREATE TRIGGER IF NOT EXISTS reduce_stock 
	AFTER INSERT ON contains
	BEGIN
		UPDATE Book SET quantity = quantity - NEW.quantity WHERE isbn = NEW.isbn;
		UPDATE Total_sales SET quantity = quantity + NEW.quantity WHERE isbn = NEW.isbn;
	END;

-- Trigger for before a book is deleted
-- This deletes the entries in wrote and genre that relate to the given book

-- I don't delete the reference to book in the sells and Total_sales
-- because I am assuming they would still need records since they still 
-- paid for the books and will be losing money
-- Only the isbn is shown in reports so it's okay that it stays
CREATE TRIGGER IF NOT EXISTS delete_book 
	BEFORE DELETE ON Book
	BEGIN
		DELETE FROM wrote WHERE isbn = OLD.isbn;
		DELETE FROM genre WHERE isbn = OLD.isbn;
	END;

-- Trigger to refund a purchase because a book is being removed
-- Removes the quantity from the sales
CREATE TRIGGER IF NOT EXISTS refund 
	AFTER DELETE ON contains
	BEGIN
		UPDATE Total_sales SET quantity = quantity - OLD.quantity WHERE isbn = OLD.isbn;
	END;