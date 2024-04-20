-- 코드를 입력하세요
SELECT ANIMAL_TYPE, 
    CASE WHEN NAME IS NULL THEN 'No name'
    else NAME
    end as NAME, 
    SEX_UPON_INTAKE
    From animal_ins
    order by animal_id asc