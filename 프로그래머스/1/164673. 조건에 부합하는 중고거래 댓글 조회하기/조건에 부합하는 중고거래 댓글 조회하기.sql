select ub.TITLE,ub.BOARD_ID,ur.REPLY_ID	,ur.WRITER_ID,ur.CONTENTS,date_format(ur.CREATED_DATE,'%Y-%m-%d') CREATED_DATE
from USED_GOODS_BOARD as ub ,USED_GOODS_REPLY as ur
where ub.board_id = ur.board_id and year(ub.CREATED_DATE)=2022 and month(ub.CREATED_DATE)=10
order by ur.CREATED_DATE ASC,ub.TITLE ASC;