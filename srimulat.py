# Srimulat (Whatsapp Group Analyzer)
# Author: Brain90
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import sys
import subprocess
from dateutil import parser

class Srimulat(object):

    def __init__(self):
        self.chatFile = open(sys.argv[1], 'r')
        self.cleanFile = open("srimulat.sql","w")
        self.currentNextLine = ""
        self.counter = 1

    def process(self):
        subprocess.call(["clear"])
        ddl_header = "drop table if exists srimulat;\n" + \
                     "create table srimulat " + \
                     "(date timestamp, " + \
                     "sender varchar,  " + \
                     "content varchar);\n" + \
                     "copy srimulat (date, sender, content) from stdin;\n"
        self.write(ddl_header)
        lineBuffer = ""
        for line in self.chatFile:
            lineBuffer = self.lineCleaner(line)
            if (self.isRecord(line)):
                while (self.nextLineIsRecord(lineBuffer) == False):
                    lineBuffer += self.lineCleaner(self.currentNextLine)
                self.write(self.recordParser(lineBuffer))
                self.write(self.recordParser(self.lineCleaner(self.currentNextLine)))
            lineBuffer = ""
        self.terminate()        

    def terminate(self):
        self.write("\.\n")
        self.cleanFile.close()
        self.chatFile.close()
        print "\n\n[Done]\nDeploy srimulat.sql to your postgres,\n" + \
              "Start playing with some sql inside ./sql directories.\n" + \
              "Have Fun !\n"
        sys.exit()

    def write(self, cleanLine):
        self.cleanFile.write(cleanLine)
        sys.stdout.write("Processing %d line \r" % (self.counter))
        sys.stdout.flush()
        self.counter += 1
        
    def lineCleaner(self, line):
        return line.strip().replace("\r",""). \
               replace("<U+202C>","").replace("<U+202A>","")

    def nextLineIsRecord(self, lineBuffer):
        try:
            self.currentNextLine = next(self.chatFile)
        except StopIteration:
            self.write(self.recordParser(lineBuffer))
            self.terminate()
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
        if (cleanContent.strip() == ''): cleanContent = '\N'
        return parser.parse(msg_date).strftime("%Y-%m-%d %H:%M") + "\t" + \
               sender + "\t" + cleanContent + "\n"

Srimulat = Srimulat();
Srimulat.process()
