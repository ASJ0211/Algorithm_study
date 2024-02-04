-- 코드를 입력하세요
SELECT MEMBER_ID,MEMBER_NAME,GENDER,DATE_FORMAT(DATE_OF_BIRTH,"%Y-%m-%d") as DATE_OF_BIRTH
from member_profile
where month(date_of_birth) = 3 and tlno is not null AND GENDER= "W"
ORDER BY MEMBER_ID ASC;
