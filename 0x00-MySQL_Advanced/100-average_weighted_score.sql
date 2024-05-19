-- script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN u_id INT)
BEGIN
    SELECT AVG(score * projects.weight) INTO @wasc
    FROM corrections
    INNER JOIN projects
    ON project_id = projects.id
    WHERE user_id = u_id;
    UPDATE
