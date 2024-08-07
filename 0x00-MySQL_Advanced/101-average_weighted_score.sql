-- Create stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users u
    SET average_score = (
        SELECT IFNULL(SUM(c.score * p.weight) / SUM(p.weight), 0)
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = u.id
    );
END //
DELIMITER ;
