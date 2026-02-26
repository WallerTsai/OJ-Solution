WITH CTE AS (
    SELECT 
        id,
        num,
        -- 序列 1：全局的连续行号（忽略断层的 id）
        ROW_NUMBER() OVER (ORDER BY id) AS r1,
        -- 序列 2：按目标字段（num）分组的连续行号
        ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS r2
    FROM Logs
)
-- 查出连续出现次数 >= 3 的数字
SELECT DISTINCT num AS ConsecutiveNums
FROM CTE
GROUP BY num, (r1 - r2) 
HAVING COUNT(*) >= 3;