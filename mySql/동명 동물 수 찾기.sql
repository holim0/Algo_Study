-- 코드를 입력하세요
SELECT a.NAME, count(a.NAME)
from ANIMAL_INS a
group by a.NAME 
having count(a.NAME) >1
order by a.NAME

