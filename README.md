# Asmuni
Whatsapp group chat analyzer

### Usage steps ###
- Export whatsapp history
- Summon asmuni
```
$ python parser.py [WhatsAppBackupFile.txt]

#Example:
$ python asmuni.py WhatsApp\ Chat\ With\ YourGroupName.txt
```
- Asmuni will give you a file called "srimulat.sql"
- Deploy those sql files to your postgres
- Start playing with some sql inside ./sql directories
- Have Fun !

### Feature ###
- Get member and total post
- Age of group
- Posted time frequency (midnight, morning, afternoon, evening, night)
- Count word frequency 
- Count Some word frequency 
- Word frequency by specific member
- Total Post Group By Member, Month, Year
- Show Busiest month  
- Most used words by some member in the morning
- Member who summon "someone" frequently
- Top 10 Busiest Days
- Content within top 1 busiest days

