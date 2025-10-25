# select ta.id,tb.fish_name, ta.length
# from fish_info as ta join fish_name_info as tb on ta.fish_type = tb.fish_type
# where ta.length in (select max(length) as mleng from fish_info group by fish_type having length = max(length))
# order by ta.id asc












select info.id,name.fish_name,info.length as length
from fish_info as info join fish_name_info as name on info.fish_type = name.fish_type
where info.fish_type in 
    (select fish_type 
     from fish_info 
     group by fish_type
    having length = max(length))