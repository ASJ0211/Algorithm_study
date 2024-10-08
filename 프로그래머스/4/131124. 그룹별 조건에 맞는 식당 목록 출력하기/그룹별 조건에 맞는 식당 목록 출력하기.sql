-- 코드를 입력하세요
with t1 as  (select member_id,count(review_id) as cr from rest_review group by member_id order by member_id desc)
select pro.member_name, review.review_text,date_format(review.review_date,'%Y-%m-%d')
from member_profile as pro join rest_review as review on pro.member_id = review.member_id join t1 on t1.member_id =pro.member_id where t1.cr = (select max(t1.cr) from t1)
order by 3 asc, 2 asc