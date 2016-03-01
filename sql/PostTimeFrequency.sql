-- Waktu posting
(SELECT 'Dini Hari' as waktu_posting, count(*) as jumlah from srimulat where extract(hour from date) >= 0 and extract(hour from date) <= 6 group by 1)
union
(SELECT 'Pagi' as waktu_posting, count(*) as jumlah from srimulat where extract(hour from date) > 6 and extract(hour from date) <= 11 group by 1)
union
(SELECT 'Siang/Sore' as waktu_posting, count(*) as jumlah from srimulat where extract(hour from date) > 11 and extract(hour from date) <= 17 group by 1)
union
(SELECT 'Malam' as waktu_posting, count(*) as jumlah from srimulat where extract(hour from date) > 17 and extract(hour from date) <= 23 group by 1);

