-- script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN u_id INT)
BEGIN
    SELECT AVG(score * projects.weight) INTO @wasc
    FROM corrections
    JOIN projects
    ON project_id = projects.id
    WHERE user_id = u_id;
    -- Storing the weighted average to the user.
    UPDATE users
    SET average_score = @wasc
    WHERE id = u_id;
END$$

DELIMITER ;
