from unittest import TestCase
from unittest_data_provider import data_provider
from tontonbot.plugins.youtube import Youtube
from tontonbot.core.security import Security


class TestYoutube(TestCase):
    def setUp(self):
        security = Security()
        self.plugin = Youtube('Youtube', None, 'A test', {}, security)

    messages = lambda: (
        ('https://www.youtube.com/watch?v=1H5loYi6wVc&feature=youtube_gdata_player', True, '1H5loYi6wVc'),
        ('https://www.youtube.com/watch?v=uNuFVq5QeRk#t=289', True, 'uNuFVq5QeRk'),
        ('https://www.youtube.com/watch?v=203QC6hYIss', True, '203QC6hYIss'),
        ('http://www.youtube.com/watch?v=203QC6hYIss', True, '203QC6hYIss'),
        ('https://youtube.com/watch?v=203QC6hYIss', True, '203QC6hYIss'),
        ('http://youtube.com/watch?v=203QC6hYIss', True, '203QC6hYIss'),
        ('youtube.com/watch?v=203QC6hYIss', True, '203QC6hYIss'),
        ('www.youtube.com/watch?v=203QC6hYIss', True, '203QC6hYIss'),
        ('titi tutu -> https://www.youtube.com/watch?v=-XyfYfuATwQ', True, '-XyfYfuATwQ'),
        ('http://www.youtube.com/watch?v=0zM3nApSvMg&feature=feedrec_grec_index', True, '0zM3nApSvMg'),
        ('http://www.youtube.com/v/0zM3nApSvMg?fs=1&amp;hl=en_US&amp;rel=0', True, '0zM3nApSvMg'),
        ('http://www.youtube.com/embed/0zM3nApSvMg?rel=0', True, '0zM3nApSvMg'),
        ('http://www.youtube.com/watch?v=0zM3nApSvMg', True, '0zM3nApSvMg'),
        ('http://youtu.be/0zM3nApSvMg', True, '0zM3nApSvMg'),
        ('pong', False, None),
    )

    @data_provider(messages)
    def test_recognize(self, message, result, data):
        self.assertEqual(self.plugin.recognize('PRIVMSG', 'toto', ['toto', message]), result)
        self.assertEqual(self.plugin.data, data)
