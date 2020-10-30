SELECT e.branch_id, sum(e.salary) as total
from employees e
group by e.branch_id
order by e.branch_id