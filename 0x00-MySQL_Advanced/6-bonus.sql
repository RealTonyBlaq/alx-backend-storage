-- script that creates a stored procedure AddBonus that adds a new correction for a student.

DELIMITER $$

CREATE PROCEDURE AddBonus ( IN user_id INT, IN project_name VARCHAR(256), IN score INT)
BEGIN
    SELECT 
