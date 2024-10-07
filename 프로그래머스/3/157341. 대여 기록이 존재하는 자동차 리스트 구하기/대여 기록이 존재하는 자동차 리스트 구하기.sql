-- 코드를 입력하세요
SELECT distinct(car.car_id)
from car_rental_company_car as car join CAR_RENTAL_COMPANY_RENTAL_HISTORY as history
on car.car_id = history.car_id
where car.car_type = "세단" and date_format(history.start_date,"%m")=10
order by car_id desc;
