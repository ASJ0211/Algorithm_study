-- 코드를 입력하세요
with ins2 as (select * from animal_ins where sex_upon_intake like'intact%'),
outs2 as  (select * from animal_outs where sex_upon_outcome like 'spayed%' or sex_upon_outcome like 'neutered%' )
select ins2.animal_id,ins2.animal_type,ins2.name from ins2 join outs2 on ins2.animal_id = outs2.animal_id