-- Frekuensi posting tiap member per bulan, per tahun
select distinct 
    sender, 
    extract(year from date) as tahun, 
    extract(month from date) as bulan, 
    count(*) as jumlah_posting 
from 
    srimulat 
group by
    sender, bulan, tahun
order by
    sender, tahun, bulan;
