# Srimulat
Whatsapp group chat analyzer using python & postgres 

### Installation ###
- [Export whatsapp history](https://www.whatsapp.com/faq/en/android/23756533)
- Summon srimulat
```
$ python srimulat.py [WhatsAppBackupFile.txt]
```
- Srimulat will give you file called "srimulat.sql"
- Deploy those sql into your postgres
- Start playing with some sql inside ./sql directories
- Have Fun !

### Feature ###
- Get member and total post
- Age of group
- Post time frequency (midnight, morning, afternoon, evening, night)
- Count word frequency 
- Count Some word frequency 
- Word frequency by specific member
- Total Post Group By Member, Month, Year
- Show Busiest month  
- Most used words by some member in the morning
- Member who summon "someone" frequently
- Top 10 Busiest Days
- Show discussion within busiest days

## Educational Purposes ###
[Gen Z](https://en.wikipedia.org/wiki/Generation_Z) student raised with social media culture. They use whatsapp, telegram, line, etc to interact with their friends, family, etc. Such tools are very close to their lifes. By using any of it as an example, teacher can attract student into programming / rdbms concept more easily. Some interesting problem to solve :

_Beginner/Intermediate topic:_
- Analyze friends personality based on posted contents (Aggregation)
- Normalize chat history tables (Normalization concept)
- Convert some srimulat feature using normal table (Intro to crud / join concept) 
- Transform query result into graphical diagram (Descriptive statistics)
- Found most active / most silent friends (Aggregation) 
- Find friends idle / busy day by aggregating their post (Aggregation)

_Advance topic :_
- Creating a word stemmer within posted content
- Performance Tuning

### Long Live Srimulat ###
![srimulatfc.jpg](https://github.com/brain90/srimulat/blob/master/srimulatfc.jpg "https://upload.wikimedia.org/wikipedia/id/8/81/SRIMULATFC.jpg")

```
Top LeftToRight : Paul - Subur - Basuki - Pak Bendot - Nurbuat - Darsono - Tarzan 
Bottom LeftToRight : Gepeng - Timbul - Sigit - Triman
```
### License ###
```
Srimulat are Teguh slamet rahardjo and Raden Ayu Srimulat trademark.
https://id.wikipedia.org/wiki/Srimulat

This work licensed in http://www.wtfpl.net/ 
```
