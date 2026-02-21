SELECT IFNULL(
    (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY Salary DESC
        LIMIT 1,1
    ), NULL
) as SecondHighestSalary;