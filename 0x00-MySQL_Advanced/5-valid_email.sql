-- script that creates a trigger that resets the attribute valid_email only when the email has been changed.

DELIMITER $$

CREATE TRIGGER reset_attribute
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF 
