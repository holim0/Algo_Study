-- 코드를 입력하세요
SELECT hour(a.DATETIME) as HOUR, count(a.DATETIME) as COUNT
from ANIMAL_OUTS a
where hour(a.DATETIME)>8 and hour(a.DATETIME)<20
group by HOUR(a.DATETIME)
order by hour(a.DATETIME) asc