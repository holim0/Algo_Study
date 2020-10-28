-- 코드를 입력하세요
SELECT distinct(c.cart_id)
from CART_PRODUCTS c, CART_PRODUCTS d
where c.name="Milk" and d.name="Yogurt"
and c.cart_id=d.cart_id
order by c.cart_id