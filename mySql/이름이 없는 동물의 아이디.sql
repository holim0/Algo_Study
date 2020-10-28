-- 코드를 입력하세요
SELECT a.ANIMAL_ID
from ANIMAL_INS a
where isnull(a.name)
order by a.animal_id asc