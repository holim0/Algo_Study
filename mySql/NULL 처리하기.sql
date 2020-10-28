-- 코드를 입력하세요
SELECT a.animal_type, IFNULL(a.name, "No name"), a.SEX_UPON_INTAKE
from ANIMAL_INS a 
order by a.animal_id