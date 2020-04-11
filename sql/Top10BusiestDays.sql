-- 10 hari paling sibuk

select distinct 
    date::date as tanggal, 
    count(*) as jumlah_posting,
    age(max(date),min(date)) as lama_percakapan
from 
    srimulat 
group by
   tanggal
order by
    jumlah_posting desc
limit 10;

