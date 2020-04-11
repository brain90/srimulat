-- Member dan total posting
select distinct sender, count(*) as total_posting from srimulat group by sender having count(*) > 1 order by 2 desc;

