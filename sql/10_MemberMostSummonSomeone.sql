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

