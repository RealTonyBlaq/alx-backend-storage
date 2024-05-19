-- script that creates a function SafeDiv that divides (and returns)
-- the first by the second number or returns 0 if the second number is equal to 0

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS INT DETERMINISTIC
RETURN IF(b = 0, );
