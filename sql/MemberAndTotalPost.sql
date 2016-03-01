-- Member dan total posting
select distinct sender, count(*) as total_posting from srimulat group by sender order by 2 desc;

