-- script that creates a stored procedure ComputeAverageScoreForUser that computes
-- and store the average score for a student. Note: An average score can be a decimal

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser ( IN u_id INT)
BEGIN
    SELECT AVG(score) INTO @my_average
    FROM corrections
    WHERE user_id = u_id;
    UPDATE users
    SET average_score = @my_average
    WHERE id = u_id;
END$$

DELIMITER ;
