---- Member dan total posting
--select distinct sender, count(*) from srimulat group by sender order by 2 desc;
--
---- Waktu posting
--SELECT 'Dini Hari', count(*) as jumlah from srimulat where extract(hour from date) >= 0 and extract(hour from date) <= 6 group by 1;
--SELECT 'Pagi', count(*) as jumlah from srimulat where extract(hour from date) > 6 and extract(hour from date) <= 11 group by 1;
--SELECT 'Siang/Sore', count(*) as jumlah from srimulat where extract(hour from date) > 11 and extract(hour from date) <= 17 group by 1;
--SELECT 'Malam', count(*) as jumlah from srimulat where extract(hour from date) > 17 and extract(hour from date) <= 23 group by 1;
--
---- Frekuensi kata
--SELECT word, count(*)
--FROM ( 
--  SELECT regexp_split_to_table(content, '\s') as word
--  FROM srimulat
--) t
--GROUP BY word order by 2 desc;
--
---- Frekuensi kata per member
--SELECT word, count(*)
--FROM ( 
--  SELECT regexp_split_to_table(target.content, '\s') as word
--  FROM 
--    (
--        select content from srimulat where sender ilike '%sudrajat%'
--    ) target 
--) t
--GROUP BY word order by 2 desc;

-- Frekuensi posting per bulan
--select distinct 
--    sender, 
--    extract(year from date) as tahun, 
--    extract(month from date) as bulan, 
--    count(*) as jumlah_posting 
--from 
--    srimulat 
--group by
--    sender, bulan, tahun
--order by
--    sender, tahun, bulan;
--
---- Bulan paling sibuk
--select distinct 
--    extract(year from date) as tahun, 
--    extract(month from date) as bulan, 
--    count(*) as jumlah_posting 
--from 
--    srimulat 
--group by
--    bulan, tahun
--order by
--    jumlah_posting desc;

-- Paling banyak diomongin member tertentu pas pagi hari

SELECT word, count(*)
FROM ( 
  SELECT regexp_split_to_table(target.content, '\s') as word
  FROM 
    (
        select content from srimulat where sender ilike '%gibran%'
        and extract(hour from date) >=7 and extract(hour from date) <=11
    ) target 
) t
GROUP BY word order by 2 desc;
