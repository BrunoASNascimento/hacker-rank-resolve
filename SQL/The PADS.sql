
(select test_name.data as data 
from
(SELECT concat(Name,'(', SUBSTRING(Occupation, 1, 1),')') as data 
from  OCCUPATIONS 
order by Name ) as test_name)
UNION all
select test.data as data from (
    select   Occupation, 
    concat('There are a total of ',count(1),' ',LOWER(Occupation),'s.') as data 
    from OCCUPATIONS 
    group by Occupation 
    order by concat('There are a total of ',count(1),' ',LOWER(Occupation),'s.')
) as test
order by data
