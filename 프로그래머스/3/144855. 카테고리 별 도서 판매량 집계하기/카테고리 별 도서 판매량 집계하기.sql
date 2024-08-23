-- 코드를 입력하세요
SELECT b.category,sum(s.sales) as total_sales
from book as b join book_sales as s on b.book_id=s.book_id
where date_format(s.sales_date,"%y%m") = "2201"
group by b.category
order by b.category ASC