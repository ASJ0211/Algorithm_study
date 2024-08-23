-- 코드를 입력하세요
SELECT b.author_id,a.author_name,b.category, sum(b.price*s.sales) as total_sales 
from book_sales as s join book as b on s.book_id = b.book_id join author as a on b.author_id = a.author_id
where date_format(s.sales_date, '%Y%m')=202201
group by b.author_id,b.category
order by b.author_id ASC, b.category DESC