-- Frekuensi kata per member tertentu
SELECT left(word,30) as word, count(*)
FROM ( 
  SELECT regexp_split_to_table(target.content, '\s') as word
  FROM 
    (
        select content from srimulat where sender ilike '%haris%'
    ) target 
) t
GROUP BY word order by 2 desc;

