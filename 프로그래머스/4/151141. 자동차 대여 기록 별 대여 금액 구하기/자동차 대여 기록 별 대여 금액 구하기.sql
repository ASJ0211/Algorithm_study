with h1 as (
    select car.car_id,his.history_id,car.car_type,car.daily_fee,timestampdiff(day,start_date,end_date)+1 as days ,
    case 
    when timestampdiff(day,start_date,end_date)+1<7 then 'NONE'
    when timestampdiff(day,start_date,end_date)+1<30 then '7일 이상'
    when timestampdiff(day,start_date,end_date)+1<90 then '30일 이상'
    else '90일 이상'
    end as days2
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY as his  join CAR_RENTAL_COMPANY_CAR as car
    on his.car_id = car.car_id
    where car.car_type = '트럭'
)
select h1.history_id,round(h1.days*h1.daily_fee*(100-ifnull(plan.discount_rate,0))/100,0) as fee
from h1 left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as plan on h1.days2 = plan.duration_type
and h1.car_type = plan.car_type
order by 2 desc, 1 desc


# #######
# WITH value AS (
#     SELECT car.daily_fee, car.car_type, his.history_id,
#            DATEDIFF(end_date, start_date) + 1 AS period,
#     CASE 
#       WHEN DATEDIFF(end_date, start_date) + 1 >= 90 THEN '90일 이상'
#       WHEN DATEDIFF(end_date, start_date) + 1 >= 30 THEN '30일 이상'
#       WHEN DATEDIFF(end_date, start_date) + 1 >= 7 THEN '7일 이상'
#       ELSE 'NONE' END AS duration_type
# FROM car_rental_company_rental_history AS his
# INNER JOIN car_rental_company_car AS car ON car.car_id = his.car_id
# WHERE car.car_type = '트럭')   

# SELECT value.history_id, 
#     ROUND(value.daily_fee * value.period * 
#           (100 - IFNULL(plan.discount_rate,0)) / 100) AS FEE
# FROM value
# LEFT JOIN car_rental_company_discount_plan AS plan 
#     ON plan.duration_type = value.duration_type 
#     AND plan.car_type = value.car_type
# ORDER BY 2 DESC, 1 DESC

