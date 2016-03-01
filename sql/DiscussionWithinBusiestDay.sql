-- Isi diskusi pada hari tersibuk 
select
     *
from
(
     select distinct
         date::date as tanggal,
         count(*) as jumlah_posting
     from
         srimulat
     group by
        tanggal
     order by
         jumlah_posting desc
     limit 1
) yippie
join 
    srimulat on srimulat.date::date = yippie.tanggal
order by
    srimulat.date asc;
