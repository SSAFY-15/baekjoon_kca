-- 코드를 입력하세요
# FIRST_HALF=f / ICECREAM_INFO =i
# FIRST_HALF.flavor =pk / ICECREAM_INFO.flavor =fk

SELECT f.FLAVOR 
from FIRST_HALF as f
join ICECREAM_INFO  as i
on f.FLAVOR = i.FLAVOR
where f.TOTAL_ORDER > 3000 
and i.INGREDIENT_TYPE = 'fruit_based'
order by f.TOTAL_ORDER desc;
