import unittest, subprocess
from ..srimulat import process

class TestProcess(unittest.TestCase):
    
    def test_process(self):
        chatHistory = "WhatsApp\ Chat\ with\ GENERASI\ SRIMULAT.txt"
        processResult = subprocess.check_output(["python ../srimulat.py " + chatHistory], shell=True)
        isFIleGenerated = subprocess.check_output(["if [ -f srimulat.sql ]; then echo true; fi"])
        self.assertEqual(("[done]" in processResult) and ("true" in isFIleGenerated), True)

if (__name__=='__main__'):
    unittest.main()
