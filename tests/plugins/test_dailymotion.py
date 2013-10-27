from unittest import TestCase
from unittest_data_provider import data_provider
from tontonbot.plugins.dailymotion import Dailymotion
from tontonbot.core.security import Security


class TestDailymotion(TestCase):
    def setUp(self):
        security = Security()
        self.plugin = Dailymotion('Dailymotion', None, 'A test', {}, security)

    messages = lambda: (
        ('http://www.dailymotion.com/video/xsw0h7_minus-et-cortex-episode-2_people?from_related=related.page.int.behavior-meta2.f01e85f97110c0f348a26713a7b819d8138212538', True, 'xsw0h7'),
        ('https://www.dailymotion.com/video/xsw0h7_minus-et-cortex-episode-2_people?from_related=related.page.int.behavior-meta2.f01e85f97110c0f348a26713a7b819d8138212538', True, 'xsw0h7'),
        ('http://dailymotion.com/video/xsw0h7_minus-et-cortex-episode-2_people', True, 'xsw0h7'),
        ('dailymotion.com/video/xsw0h7_minus-et-cortex-episode-2_people', True, 'xsw0h7'),
        ('pong', False, None),
    )

    @data_provider(messages)
    def test_recognize(self, message, result, data):
        self.assertEqual(self.plugin.recognize('PRIVMSG', 'toto', ['toto', message]), result)
        self.assertEqual(self.plugin.data, data)

