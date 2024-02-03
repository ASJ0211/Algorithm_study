-- 코드를 입력하세요
SELECT PT_NAME,PT_NO,GEND_CD,AGE,IFNULL(tlno,'NONE') as tlno from patient where age<=12 AND GEND_CD='W'order by age desc,pt_name ASC;
