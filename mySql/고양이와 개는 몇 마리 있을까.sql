-- 코드를 입력하세요
SELECT a.ANIMAL_TYPE, count(a.ANIMAL_TYPE)
from ANIMAL_INS a
group by a.ANIMAL_TYPE
order by a.ANIMAL_TYPE