-- script that creates a trigger that decreases the quantity of an item after adding a new order.

CREATE TRIGGER update_items
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE TABLE items
SET quantity =
