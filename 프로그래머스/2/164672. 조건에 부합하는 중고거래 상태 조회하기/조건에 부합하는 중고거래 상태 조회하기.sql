-- 코드를 입력하세요
SELECT BOARD_ID,	WRITER_ID,	TITLE,	PRICE,
    (case when status = 'done' then '거래완료'
    when status = 'reserved' then '예약중'
    when status = 'sale' then '판매중'
    end) as status
from used_goods_board
where date(created_date) ='2022-10-05'
order by board_id desc