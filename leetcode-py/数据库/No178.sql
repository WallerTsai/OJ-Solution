SELECT 
    S.score,
    dense_rank() over (order by S.score DESC) as 'rank'
FROM Scores S;


SELECT 
    s1.score,
    (
        SELECT COUNT(DISTINCT s2.score)
        FROM Scores s2
        WHERE s2.score >= s1.score
    ) as "rank"
FROM
    Scores s1
ORDER BY
    s1.score DESC