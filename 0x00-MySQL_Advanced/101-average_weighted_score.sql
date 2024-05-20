-- script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    FOR EACH ROW IN 
