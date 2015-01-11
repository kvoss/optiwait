import re
import unittest

# from dateutil.parser import parse

import logging

logger = logging.getLogger(__name__)

__all__ = ['Parser']

PATTERN = re.compile(r'(\d+)\s*min')

PATTERNH = re.compile(r'(\d+)\s*(hour|hr)')
PATTERN1H = re.compile(r'\b(one|an)\s+(hour|hr)\b')

class Parser(object):

    def __init__(self, txt):
        self.txt = txt.lower()

    def get_minutes(self):
        DEFAULT_WAIT = 66

        sre = PATTERN.search(self.txt)
        sreh = PATTERNH.search(self.txt)
        sre1h = PATTERN1H.search(self.txt)
        #print txt
        if sre:
            mins = sre.groups(1)
            mins = int( mins[0])
        elif sreh:
            hours = sreh.groups(1)
            mins = int(hours[0]) * 60
        elif sre1h:
            mins = 60
        else:
            mins = DEFAULT_WAIT
            logger.debug('default wait: ' + self.txt)

        return mins


 
class TestParser(unittest.TestCase):
    """
    I take tests from https://twitter.com/mediclinicon8th
    """
 
    def setUp(self):
        pass

    def test_45min(self):
        txt = '45min wait at 10:51 am.'
        self.assertEqual( Parser(txt).get_minutes(), 45)

    def test_60_to_90(self):
        txt = "wait time at 12:47 pm is 60 to 90 mins"
        self.assertEqual( Parser(txt).get_minutes(), 90)
 
    def test_an_hour(self):
        txt = "It's at least an hour wait at 10:45am"
        self.assertEqual( Parser(txt).get_minutes(), 60)
 
    def test_one_hr(self):
        txt = 'still one hour wait'
        self.assertEqual( Parser(txt).get_minutes(), 60)
 
    def test_2hr(self):
        txt = 'still 2hr wait'
        self.assertEqual( Parser(txt).get_minutes(), 120)
 
    def test_45dash60_min(self):
        txt = 'Wait time is about 45-60 minutes.'
        self.assertEqual( Parser(txt).get_minutes(), 60)

    def test_fractional(self):
        txt = 'Our wait time is 1 hour to 1 1/2 hours @ 5:47 pm.'
        self.assertEqual( Parser(txt).get_minutes(), 60)

    def test_empty_room(self):
        txt = 'We have an empty waiting room at 1:05pm!!'
        self.assertEqual( Parser(txt).get_minutes(), 0)

 

if __name__ == '__main__':
    unittest.main()

