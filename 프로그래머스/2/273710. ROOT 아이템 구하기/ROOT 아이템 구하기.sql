-- 코드를 작성해주세요
select ti.item_id,ti.item_name
from item_info as ti
join 
item_tree as tt on ti.item_id = tt.item_id
where tt.item_id in (select item_id
                   from item_tree
                   where isnull(parent_item_id) = 1               
                  )
