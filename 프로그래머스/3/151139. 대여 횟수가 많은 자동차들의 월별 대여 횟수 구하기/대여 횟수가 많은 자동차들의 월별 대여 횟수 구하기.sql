-- 코드를 입력하세요
SELECT date_format(start_date,"%m") as month,car_id, count(start_date) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as rent
where car_id in (select car_id
                 from CAR_RENTAL_COMPANY_RENTAL_HISTORY as rent0
                 WHERE DATE_FORMAT(start_date, "%Y-%m") BETWEEN '2022-08' AND '2022-10' 
                 group by rent0.car_id
                 having count(history_id)>=5
               )
AND DATE_FORMAT(start_date, "%Y-%m") BETWEEN '2022-08' AND '2022-10'
group by month,car_id
order by month ASC, car_id DESC
