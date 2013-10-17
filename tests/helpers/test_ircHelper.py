from unittest import TestCase
from tontonbot.helpers import irc_helper


class TestIrcHelper(TestCase):
    def test_extract_nickname(self):
        self.assertEqual(irc_helper.IrcHelper.extract_nickname('tonton!qdmljazo'), 'tonton')

    def test_extract_sender(self):
        self.assertEqual(irc_helper.IrcHelper.extract_sender('tonton', '#toto', 'tutu'), '#toto')
        self.assertEqual(irc_helper.IrcHelper.extract_sender('tonton', 'tutu', 'tutu'), 'tonton')

    def test_extract_message(self):
        self.assertEqual(irc_helper.IrcHelper.extract_message(['#tutu', 'toto']), 'toto')
