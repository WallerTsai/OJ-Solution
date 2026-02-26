SELECT 
    a.name as Employee
FROM
    Employee a, Employee b
WHERE
    a.managerID = b.id and a.salary > b.salary