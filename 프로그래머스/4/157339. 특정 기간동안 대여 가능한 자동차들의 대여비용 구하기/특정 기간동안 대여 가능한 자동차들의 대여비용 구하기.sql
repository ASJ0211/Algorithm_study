
-- 코드를 입력하세요
with tc as(
select * from CAR_RENTAL_COMPANY_CAR
where car_type ='세단' or car_type ='SUV'
), th as(
select * from CAR_RENTAL_COMPANY_rental_history
where date_format(end_date,'%m') >=11 or year(end_date) = 2023
), tp as(
select * from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
where duration_type = '30일 이상'
)
#select tc.car_id,tc.car_type,tc.daily_fee,tp.discount_rate,(tc.daily_fee*30/100*(100-tp.discount_rate) ) as FEE
select distinct tc.car_id as CAR_ID,tc.car_type as CAR_TYPE,round((tc.daily_fee*30*((100-tp.discount_rate)/100) ),0) as FEE
from tc join CAR_RENTAL_COMPANY_RENTAL_HISTORY as his on tc.car_id = his.car_id join tp on tc.car_type = tp.car_type
where his.car_id not in (select car_id from th) and tc.car_type = tp.car_type and tc.car_id
in (

select tc.car_id
from tc join CAR_RENTAL_COMPANY_RENTAL_HISTORY as his on tc.car_id = his.car_id join tp on tc.car_type = tp.car_type
where tc.daily_fee*30/100*(100-tp.discount_rate)<2000000 and tc.daily_fee*30/100*(100-tp.discount_rate)>=500000

)
order by fee desc,car_type asc, car_id desc;