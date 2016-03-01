-- Umur grup srimulat
select 
    age(max(date)::date, min(date)::date)
from
    srimulat;

