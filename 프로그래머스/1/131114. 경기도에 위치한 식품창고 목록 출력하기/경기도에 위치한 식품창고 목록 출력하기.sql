-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, ifnull(FREEZER_YN,'N') as freezer_yn
from food_warehouse
where left(address,3) = '경기도'
order by WAREHOUSE_ID ASC
