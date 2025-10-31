-- 코드를 입력하세요
SELECT tb.BOOK_ID	,ta.AUTHOR_NAME,	date_format(tb.PUBLISHED_DATE,'%Y-%m-%d' )
from book as tb
left join author as ta on tb.author_id = ta.author_id
where tb.category = '경제'
order by published_date asc
