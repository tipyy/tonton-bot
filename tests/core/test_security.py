from unittest import TestCase
from tontonbot.core.security import *


class TestSecurity(TestCase):
    def setUp(self):
        self.security = Security()

    def test_addToBlackList(self):
        self.security.addToBlackList('toto')
        expected = ['toto']

        self.assertEqual(self.security.black_list, expected)

    def test_addToWhiteList(self):
        self.security.addToWhiteList('toto')
        expected = ['toto']

        self.assertEqual(self.security.white_list, expected)

    def test_addEvent(self):
        self.security.addEvent('JOIN')
        expected = ['JOIN']

        self.assertEqual(self.security.event_list, expected)

    def test_checkSecurity(self):
        self.security = Security()
        self.assertEqual(self.security.checkSecurity('tonton', 'JOIN'), True)
        self.security.addEvent('JOIN')
        self.assertEqual(self.security.checkSecurity('tonton', 'PRIVMSG'), False)
        self.assertEqual(self.security.checkSecurity('tonton', 'JOIN'), True)
        self.security.addToBlackList('tonton')
        self.assertEqual(self.security.checkSecurity('tonton', 'JOIN'), False)
        self.security = Security()
        self.security.addToWhiteList('toto')
        self.assertEqual(self.security.checkSecurity('tonton', 'JOIN'), False)
        self.security.addToWhiteList('tonton')
        self.assertEqual(self.security.checkSecurity('tonton', 'JOIN'), True)