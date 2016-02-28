import re
import sys
import sqlite3
from datetime import datetime
from dateutil import parser

class Asmuni(object):

    currentNextLine = ""

    def __init__(self, chatFile):
        self.chatFile = chatFile

    def process(self):
        chatFile = open(self.chatFile, 'r')
        cleanFile = open("cleanFile.txt","w")

        lineBuffer = ""
        for line in chatFile:
            line = self.lineCleaner(line) 
            lineBuffer = line
            if (self.isRecord(line)):
                while (self.nextLineIsRecord(chatFile) == False):
                    lineBuffer += self.lineCleaner(self.currentNextLine)
                cleanFile.write(self.recordParser(lineBuffer))
                cleanFile.write(self.recordParser(self.lineCleaner(self.currentNextLine)))
            lineBuffer = ""
        cleanFile.close()
        print "done"
    
    def lineCleaner(self, line):
        return line.strip().replace("\r","")

    def nextLineIsRecord(self, chatFile):
        self.currentNextLine = next(chatFile)
        return self.isRecord(self.currentNextLine) 
        
    def isRecord(self, line):
        if (re.match('^(\d{1,2})[/.-](\d{1,2})[/.-](\d{4})',line) is not None):
            return True
        else:
            return False

    def recordParser(self, line):
        msg_date, sep, msg = line.partition(" - ")
        sender, sep, content = msg.partition(": ")
        patternNonAscii = re.compile(r'[^\x00-\x7F]+')

        contentWithoutNonAscii = patternNonAscii.sub('',content)  
        cleanContent = ' '.join(contentWithoutNonAscii.split()) 
        
        return parser.parse(msg_date).strftime("%Y-%m-%d %H:%M") + "\t" + \
               sender + "\t" + cleanContent + "\n"

        #return "INSERT INTO srimulat (date, sender, content) VALUES ('" + \
        #        parser.parse(msg_date).strftime("%Y-%m-%d %H:%M") + "',$$" + \
        #        sender + "$$,$$ " + cleanContent + " $$);\n"
    

    def recordParser2(self, line):
        msg_date, sep, msg = line.partition(" - ")
        sender, sep, content = msg.partition(": ")
        re.sub(r'[^\x00-\x7F]+','', content)
        return "INSERT INTO srimulat " + \
                "VALUES " + \
                "('" + parser.parse(msg_date).strftime("%Y-%m-%d %H:%M") + "',$$" + \
                sender + \
                "$$,$$" + content.replace('\r','') + " $$);\n";

Asmuni = Asmuni('b.txt');
Asmuni.process()
