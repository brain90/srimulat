-- Paling banyak diomongin member tertentu ketika pagi
SELECT left(word, 30), count(*)
FROM ( 
  SELECT regexp_split_to_table(target.content, '\s') as word
  FROM 
    (
        select content from srimulat where sender ilike '%sudrajat%'
        and extract(hour from date) >=7 and extract(hour from date) <=11
    ) target 
) t
GROUP BY word order by 2 desc;
