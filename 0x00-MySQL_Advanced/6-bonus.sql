-- script that creates a stored procedure AddBonus that adds a new correction for a student

DELIMITER $$

CREATE PROCEDURE AddBonus ( IN user_id INT, IN project_name VARCHAR(256), IN score INT)
BEGIN
    SELECT id INTO @my_project_id 
    FROM projects WHERE name = project_name;
    IF @my_project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET @my_project_id = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, @my_project_id, score);
END$$

DELIMITER ;
