# Srimulat
Whatsapp group chat analyzer using python & postgres 

### Usage steps ###
- (Export whatsapp history)[https://www.whatsapp.com/faq/en/android/23756533]
- Summon srimulat
```
$ python srimulat.py [WhatsAppBackupFile.txt]

#Example:
$ python srimulat.py WhatsApp\ Chat\ With\ YourGroupName.txt
```
- srimulat will give you a file called "srimulat.sql"
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
- Show discussion within busiest days

