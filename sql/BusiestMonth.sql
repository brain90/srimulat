-- Bulan paling sibuk
select distinct 
    extract(year from date) as tahun, 
    extract(month from date) as bulan, 
    count(*) as jumlah_posting 
from 
    srimulat 
group by
    bulan, tahun
order by
    jumlah_posting desc;

