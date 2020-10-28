-- 코드를 입력하세요
SELECT a.animal_id
from animal_ins a
where not isnull(a.name)

order by a.animal_id asc