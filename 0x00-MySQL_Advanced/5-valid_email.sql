-- script that creates a trigger that resets the attribute valid_email only when the email has been changed.

DELIMITER $$

CREATE TRIGGER reset_attribute
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF EXISTS NEW.email AND NEW.email != OLD.email THEN
        IF OLD.valid_email = 0 THEN
            SET valid_email = 1
        ELSE
            SET valid_email = 0
        END IF;
    END IF;
END
