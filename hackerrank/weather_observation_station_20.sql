-- Question: https://www.hackerrank.com/challenges/weather-observation-station-20

-- Solution: 
-- Run a row number counter over an ordered lat_n 
-- Query the rank at the middle of the whole rows or (num_rows + 1) / 2

select ROUND(s.LAT_N, 4)
from (
    select lat_n, row_number() over (order by LAT_N) as n
    from station
) as s
where s.n = (
    select (count(*) + 1) / 2 from station
)