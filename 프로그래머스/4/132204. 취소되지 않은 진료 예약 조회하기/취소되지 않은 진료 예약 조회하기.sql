-- 코드를 입력하세요

with a1 as (select * from appointment 
where apnt_cncl_yn = 'N' and date_format(apnt_ymd,'%Y-%m-%d') = '2022-04-13')
select a1.APNT_NO,patient.PT_NAME	,patient.PT_NO,doctor.MCDP_CD,doctor.DR_NAME,a1.APNT_YMD
from a1 join patient on patient.pt_no = a1.pt_no 
join doctor on  a1.mddr_id =doctor.dr_id
order by 6 asc