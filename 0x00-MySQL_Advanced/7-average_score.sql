-- script that creates a stored procedure ComputeAverageScoreForUser that computes
-- and store the average score for a student. Note: An average score can be a decimal

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser ( user_id INT)
BEGIN
    SELECT AVERAGE()
