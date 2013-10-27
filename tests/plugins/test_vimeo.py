from unittest import TestCase
from unittest_data_provider import data_provider
from tontonbot.plugins.vimeo import Vimeo
from tontonbot.core.security import Security


class TestVimeo(TestCase):
    def setUp(self):
        security = Security()
        self.plugin = Vimeo('Vimeo', None, 'A test', {}, security)

    messages = lambda: (
        ('http://vimeo.com/48237094', True, '48237094'),
        ('https://vimeo.com/48237094', True, '48237094'),
        ('vimeo.com/48237094', True, '48237094'),
        ('http://www/vimeo.com/48237094', True, '48237094'),
        ('http://player.vimeo.com/video/48237094', True, '48237094'),
        ('pong', False, None),
    )

    @data_provider(messages)
    def test_recognize(self, message, result, data):
        self.assertEqual(self.plugin.recognize('PRIVMSG', 'toto', ['toto', message]), result)
        self.assertEqual(self.plugin.data, data)

