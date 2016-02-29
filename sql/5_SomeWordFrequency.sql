-- Frekuensi kata "cyin" di semua posting
SELECT word, count(*)
FROM ( 
  SELECT regexp_split_to_table(content, '\s') as word
  FROM srimulat
) t
WHERE 
    word ilike '%cyin%'
GROUP BY word order by 2 desc;

