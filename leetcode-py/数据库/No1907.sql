

select 'Low Salary' as category,
        count(*) as accounts_count  
        from Accounts
        where income<20000

union 

select 'Average Salary' as category,
        count(*) as accounts_count  
        from Accounts
        where income between 20000 and 50000

union

select 'High Salary' as category,
        count(*) as accounts_count  
        from Accounts
        where income > 50000



select 'Low Salary' category, sum(income < 20000) accounts_count
from accounts
union all
select 'Average Salary', sum(income >= 20000 and income <= 50000)
from accounts
union all
select 'High Salary', sum(income > 50000)
from accounts
