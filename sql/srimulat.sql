-- Member dan total posting
select distinct sender, count(*) as total_posting from srimulat group by sender order by 2 desc;

-- Waktu posting
(SELECT 'Dini Hari' as waktu_posting, count(*) as jumlah from srimulat where extract(hour from date) >= 0 and extract(hour from date) <= 6 group by 1)
union
(SELECT 'Pagi' as waktu_posting, count(*) as jumlah from srimulat where extract(hour from date) > 6 and extract(hour from date) <= 11 group by 1)
union
(SELECT 'Siang/Sore' as waktu_posting, count(*) as jumlah from srimulat where extract(hour from date) > 11 and extract(hour from date) <= 17 group by 1)
union
(SELECT 'Malam' as waktu_posting, count(*) as jumlah from srimulat where extract(hour from date) > 17 and extract(hour from date) <= 23 group by 1);

-- Frekuensi kata di semua posting
SELECT word, count(*)
FROM ( 
  SELECT regexp_split_to_table(content, '\s') as word
  FROM srimulat
) t
GROUP BY word order by 2 desc;

-- Frekuensi kata "cyin" di semua posting
SELECT word, count(*)
FROM ( 
  SELECT regexp_split_to_table(content, '\s') as word
  FROM srimulat
) t
WHERE 
    word ilike '%cyin%'
GROUP BY word order by 2 desc;

-- Frekuensi kata per member tertentu
SELECT word, count(*)
FROM ( 
  SELECT regexp_split_to_table(target.content, '\s') as word
  FROM 
    (
        select content from srimulat where sender ilike '%sudrajat%'
    ) target 
) t
GROUP BY word order by 2 desc;

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

-- Paling banyak diomongin member tertentu ketika pagi
SELECT word, count(*)
FROM ( 
  SELECT regexp_split_to_table(target.content, '\s') as word
  FROM 
    (
        select content from srimulat where sender ilike '%sudrajat%'
        and extract(hour from date) >=7 and extract(hour from date) <=11
    ) target 
) t
GROUP BY word order by 2 desc;

-- Member paling banyak sumon pak toosa
select
    distinct sender,
    sum(sub_total) as jumlah_summon_pak_toosa
from
(
    select 
        sender, 
        count(*) as sub_total
    from 
        srimulat 
    where 
        content ilike '%toosa%'
    group by
        sender,
        content
) yippie
group by
    sender
order by
    jumlah_summon_pak_toosa desc;

-- 10 hari paling sibuk
select distinct 
    date::date as tanggal, 
    count(*) as jumlah_posting 
from 
    srimulat 
group by
   tanggal 
order by
    jumlah_posting desc
limit 10;

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

-- Umur grup srimulat
select 
    age(max(date)::date, min(date)::date)
from
    srimulat;
 
-- member, max_posting_month, min_posting_month, avg_post_per_month
