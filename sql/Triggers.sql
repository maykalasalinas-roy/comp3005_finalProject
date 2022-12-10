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