from unittest import TestCase
from tontonbot.plugins.dailymotion import Dailymotion
from tontonbot.core.security import Security


class TestYoutube(TestCase):
    def test_recognize(self):
        security = Security()
        plugin = Dailymotion("Dailymotion", None, "A test", {}, security)

        self.assertEqual(plugin.recognize("PRIVMSG", "toto", ["toto",
                                                              "http://www.dailymotion.com/video/xsw0h7_minus-et-cortex-episode-2_people?from_related=related.page.int.behavior-meta2.f01e85f97110c0f348a26713a7b819d8138212538"]),
                         True)
        self.assertEqual(plugin.data, 'xsw0h7')

        self.assertEqual(
            plugin.recognize("PRIVMSG", "toto", ["toto", "https://www.dailymotion.com/video/xsw0h7_minus-et-cortex-episode-2_people?from_related=related.page.int.behavior-meta2.f01e85f97110c0f348a26713a7b819d8138212538"]), True)
        self.assertEqual(plugin.data, 'xsw0h7')

        self.assertEqual(plugin.recognize("PRIVMSG", "toto", ["toto", "pong"]),
                         False)
