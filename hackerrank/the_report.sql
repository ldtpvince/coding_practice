-- Question: https://www.hackerrank.com/challenges/the-report/problem

-- Solution:
-- - We can use join with any compare expression
-- - Order by desc or asc should follow by the column_name (column_name order will be the order the query sort data)

select if(grade >= 8, name, 'NULL'), grade, marks
from students s
join grades g
on s.marks <= max_mark and s.marks >= min_mark
order by grade desc, name asc 