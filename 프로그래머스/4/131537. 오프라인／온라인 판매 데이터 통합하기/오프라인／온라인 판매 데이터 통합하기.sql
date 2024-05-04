(select date_format(sales_date,'%Y-%m-%d') as sales_date,product_id,user_id,sales_amount
from online_sale where month(sales_date)=3
union all
select date_format(sales_date,'%Y-%m-%d') as sales_date,product_id,NULL as user_id,sales_amount
from offline_sale where month(sales_date)=3
)   order by sales_date asc,product_id asc,user_id asc; 