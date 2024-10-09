with t1 as (SELECT * from food_order
where date_format(food_order.produce_date,'%Y-%m') = '2022-05')
select t1.product_id,pro.product_name, sum(t1.amount*pro.price) as total_sales
from t1 join food_product as pro on t1.product_id =pro.product_id 
      
group by pro.product_name
order by 3 desc ,1 asc