# -- 코드를 입력하세요
SELECT t1.car_id, round(avg(t2.duration),1) as avg_duration
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as t1
left join (select history_id,car_id, datediff(end_date,start_date)+1 as duration
      from CAR_RENTAL_COMPANY_RENTAL_HISTORY) as t2 on t1.history_id = t2.history_id
group by t1.car_id
having avg(duration)>=7
order by avg_duration DESC,t1.car_id DESC