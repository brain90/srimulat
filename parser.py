import re
import sys
from datetime import datetime
from dateutil import parser

class WhatsappChatParser(object):

    def __init__(self, chatFile):
        self.chatFile = chatFile

    def process(self):
      chatFile = open(self.chatFile, 'r')
      cleanFile = open("cleanFile.txt","w")

      # Move pointer to 3rd line
      #for i in xrange(23):
      #  chatFile.next()

      lineBuffer = ""
      counter = 0
      for line in chatFile:
        line = line.strip().replace("\r","")
        if (self.isNewRecord(line)):
          cleanFile.write(self.lineCleaner(lineBuffer+"\n"+line))
          #cleanFile.write(self.lineCleaner(line))
          lineBuffer = ""
        else:
          lineBuffer = lineBuffer + " "  + line
        counter += 1
        #print counter
      cleanFile.close()
      print "done"
                     
    def isNewRecord(self, line):
        if (re.match('^(\d{1,2})[/.-](\d{1,2})[/.-](\d{4})',line) is not None):
            return True
        else:
            return False

    def lineCleaner(self, line):
        msg_date, sep, msg = line.partition(" - ")
        sender, sep, content = msg.partition(": ")
        print line
        re.sub(r'[^\x00-\x7F]+','', content)
        return "INSERT INTO srimulat " + \
                "VALUES " + \
                "('" + parser.parse(msg_date).strftime("%Y-%m-%d %H:%M") + "','" + \
                sender + \
                "',$$" + content.replace('\r','') + "$$);";

ChatParser = WhatsappChatParser('message.txt');
ChatParser.process()
