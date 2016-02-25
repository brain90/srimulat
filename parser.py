import re
import sys
from datetime import datetime
from dateutil import parser

class WhatsappChatParser(object):

    def __init__(self, chatFile):
        self.chatFile = chatFile
        self.counter = 0

    def process(self):
      chatFile = open(self.chatFile, 'r')
      lineBuffer = ""
      cleanFile = open("cleanFile.txt","w")
      chatFile.next() 
      chatFile.next()
      for line in chatFile:
        line = line.rstrip()
        sys.exit()
        if (self.isNewRecord(line)):
          cleanFile.write(lineBuffer+"\n")
          cleanFile.write(line)
          lineBuffer = ""
        else:
          lineBuffer = lineBuffer + " "  + line
        self.lineCleaner(lineBuffer)
        print self.counter
        self.counter = self.counter + 1
      cleanFile.close()
      print "done"
                     
    def isNewRecord(self, line):
        if (re.match('^(\d{1,2})[/.-](\d{1,2})[/.-](\d{4})',line.strip()) is not None):
            return True
        else:
            return False

    def lineCleaner(self, line):
        msg_date, sep, msg = line.partition("- ")
        raw_date, sep, time = msg_date.partition(" ")
        sender, sep, content = msg.partition(": ")
        datetime_obj = parser.parse(msg_date)
        re.sub(r'[^\x00-\x7F]+','', content)
        return datetime_obj.strftime("%Y-%m-%d %H:%M") + "\t" + \
               sender + "\t" + content.replace('\r','') 


ChatParser = WhatsappChatParser('message.txt');
ChatParser.process()
