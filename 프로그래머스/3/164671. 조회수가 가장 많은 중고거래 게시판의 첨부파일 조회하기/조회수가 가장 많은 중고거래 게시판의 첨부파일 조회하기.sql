with b1 as (
    select * from USED_GOODS_BOARD  where USED_GOODS_BOARD.views in (
        select max(views) from USED_GOODS_BOARD
    )
           )
select CONCAT('/home/grep/src/',file.board_id,'/',file.file_id,file.file_name,file.file_ext) as file_path from b1 join USED_GOODS_FILE as file on b1.board_id = file.board_id
order by 1 desc