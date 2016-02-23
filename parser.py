import re
import sys

class WhatsappChatParser(object):

    def __init__(self, chatFile):
        self.chatFile = chatFile
        self.counter = 0

    def process(self):
      chatFile = open(self.chatFile, 'r')
      lineBuffer = ""
      cleanFile = open("cleanFile.txt","w")
      for line in chatFile:
        line = line.rstrip()
        if (self.isNewRecord(line)):
          cleanFile.write(lineBuffer+"\n")
          cleanFile.write(line)
          lineBuffer = ""
        else:
          lineBuffer = lineBuffer + " "  + line
        print self.counter
        self.counter = self.counter + 1
      cleanFile.close()
      print "done"
                     
    def isNewRecord(self, line):
        if (re.match('^(\d{1,2})[/.-](\d{1,2})[/.-](\d{4})',line.strip()) is not None):
            return True
        else:
            return False

ChatParser = WhatsappChatParser('srimulat.txt');
ChatParser.process()
