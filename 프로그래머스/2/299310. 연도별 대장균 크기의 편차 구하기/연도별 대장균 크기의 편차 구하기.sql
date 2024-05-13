with t1 as  (select year(DIFFERENTIATION_DATE) as year, max(SIZE_OF_COLONY) as ms
from ECOLI_DATA group by year),
t2 as (select ID,PARENT_ID,	SIZE_OF_COLONY,	year(DIFFERENTIATION_DATE) as year,	GENOTYPE from ECOLI_DATA)
select t1.year as YEAR, (t1.ms-t2.size_of_colony) as YEAR_DEV ,t2.ID
from t2 join t1 on t2.year = t1.year
order by year asc ,year_dev asc;