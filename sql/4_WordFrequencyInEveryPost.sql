-- Frekuensi kata di semua posting
SELECT left(word,30) as word, count(*)
FROM ( 
  SELECT regexp_split_to_table(content, '\s') as word
  FROM srimulat
) t 
GROUP BY word order by 2 desc;

