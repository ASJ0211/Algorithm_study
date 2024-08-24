SELECT category,price as max_price,product_name
from food_product
where category in ('과자', '국', '김치', '식용유') and category in (select category from food_product group by category having price = max(price))
group by category
order by price desc
