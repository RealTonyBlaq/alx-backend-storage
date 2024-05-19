-- script that creates a stored procedure ComputeAverageScoreForUser that computes
-- and store the average score for a student. Note: An average score can be a decimal

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser ( user_id INT)
BEGIN
    SELECT (SUM(score)  INTO @my_average
    FROM corrections
    WHERE user_id = user_id;
    UPDATE users
    SET average_score = @my_average
    WHERE id = user_id;
END$$

DELIMITER ;
