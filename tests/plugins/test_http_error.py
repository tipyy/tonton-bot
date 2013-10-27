from unittest import TestCase
from unittest_data_provider import data_provider
from tontonbot.plugins.http_error import HttpError
from tontonbot.core.security import Security


class TestHttpError(TestCase):
    def setUp(self):
        security = Security()
        self.plugin = HttpError('HttpError', None, 'A test', {}, security)

    messages = lambda: (
        ('https://gist.github.com/uogbuji/705383', True, 'https://gist.github.com/uogbuji/705383'),
        ('http://gist.github.com/uogbuji/705383', True, 'http://gist.github.com/uogbuji/705383'),
        ('gist.github.com/uogbuji/705383', True, 'gist.github.com/uogbuji/705383'),
        ('www.github.com/uogbuji/705383', True, 'www.github.com/uogbuji/705383'),
        ('titi toto tutu -> www.github.com/uogbuji/705383', True, 'www.github.com/uogbuji/705383'),
        ('pong', False, None),
    )

    @data_provider(messages)
    def test_recognize(self, message, result, data):
        self.assertEqual(self.plugin.recognize('PRIVMSG', 'toto', ['toto', message]), result)
        self.assertEqual(self.plugin.data, data)

