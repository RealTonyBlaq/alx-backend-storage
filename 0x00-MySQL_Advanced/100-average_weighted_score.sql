-- script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN u_id INT)
BEGIN
    SELECT SUM(weight) INTO @wght FROM projects;
    SELECT SUM(score * projects.weight / @wght) INTO @wasc
    FROM corrections
    RIGHT JOIN projects
    ON corrections.project_id = projects.id
    WHERE corrections.user_id = u_id;

    -- Storing the weighted average to the user.
    UPDATE users
    SET average_score = @wasc
    WHERE id = u_id;
END$$

DELIMITER ;
