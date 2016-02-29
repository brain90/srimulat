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

