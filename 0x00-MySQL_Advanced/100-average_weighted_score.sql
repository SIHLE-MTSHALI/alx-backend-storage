-- Create stored procedure ComputeAverageWeightedScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_weighted_score FLOAT;
    
    SELECT SUM(c.score * p.weight) / SUM(p.weight)
    INTO avg_weighted_score
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;
    
    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = user_id;
END //
DELIMITER ;
