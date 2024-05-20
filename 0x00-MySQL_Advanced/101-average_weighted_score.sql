-- script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECL
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN user_cursor;

    read_loop: LOOP
        FETCH user_cursor INTO u_id;

        IF DONE THEN
            LEAVE read_loop;
        END IF;

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
    END LOOP read_loop;
END$$

DELIMITER ;
