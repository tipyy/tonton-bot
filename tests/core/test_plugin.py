from unittest import TestCase
from tontonbot.core.plugin import *
from tontonbot.core.security import *


class TestPlugin(TestCase):
    def test_recognize(self):
        security = Security()
        plugin = Plugin("!command", "A test", {}, security)
        self.assertEqual(plugin.recognize("PRIVMSG", "toto", ["toto", "!command"]), True)
        self.assertEqual(plugin.recognize("PRIVMSG", "toto", ["toto", "titi"]), False)

        plugin = Plugin(None, "A test", {}, security)
        self.assertEqual(plugin.recognize("PRIVMSG", "toto", []), True)
