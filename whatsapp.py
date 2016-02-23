from datetime import datetime
from dateutil import parser
import message
import sys
import re

''' A line can be either: 
        09/12/2012 17:03:48: Sender Name: Message
        3/24/14, 1:59:59 PM: Sender Name: Message
        24/3/14, 13:59:59: Sender Name: Message
'''

class ParserWhatsapp():

    def __init__(self, raw_messages):
        self.raw_messages = raw_messages

    def parse(self):
        list_of_messages = []
        set_of_senders = set()
        toDB = open("todb.csv","w")
        for l in self.raw_messages:
            msg_date, sep, msg = l.partition(": ")
            raw_date, sep, time = msg_date.partition(" ")
            sender, sep, content = msg.partition(": ")
            datetime_obj = parser.parse(msg_date)
            re.sub(r'[^\x00-\x7F]+','', content)
            toDB.write("INSERT INTO srimulat (date,sender,content) values (" + "'" + datetime_obj.strftime("%Y-%m-%d %H:%M") + "',$$ " + sender + " $$,$$ " + content.replace('\r','')+" $$);\n") 
            print("tanggal: ", datetime_obj.strftime("%Y-%m-%d %H:%M"), " sender: ", sender, " content: ", content.replace('\r','')) 
            set_of_senders.add(sender)
            list_of_messages.append(message.Message(sender, content, raw_date, time, datetime_obj))
        toDB.close()
        sys.exit()
        return list(set_of_senders), list_of_messages
