-- 코드를 입력하세요
SELECT A.NAME, A.DATETIME
from ANIMAL_INS A
left join ANIMAL_OUTS B on A.ANIMAL_ID = B.ANIMAL_ID
where B.ANIMAL_ID is null
order by A.DATETIME asc
limit 3