-- script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    FOR EACH ROW (SELECT id FROM users;) INTO @u_id
        SELECT SUM(weight) INTO @wght FROM projects;
        SELECT SUM(score * projects.weight / @wght) INTO @wasc
        FROM corrections
        RIGHT JOIN projects
        ON corrections.project_id = projects.id
        WHERE corrections.user_id = u_id;

        -- Storing the weighted average to the user
        UPDATE users
        SET average_score = @wasc
        WHERE id = u_id;
END$$

DELIMITER ;
