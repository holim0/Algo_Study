-- 코드를 입력하세요
SELECT B.ANIMAL_ID, B.NAME
from ANIMAL_INS A
right join ANIMAL_OUTS B
on A.ANIMAL_ID = B.ANIMAL_ID
where A.ANIMAL_ID is null
order by B.ANIMAL_ID