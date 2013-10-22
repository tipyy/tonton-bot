from unittest import TestCase
from tontonbot.plugins.youtube import Youtube
from tontonbot.core.security import Security


class TestYoutube(TestCase):
    def test_recognize(self):
        security = Security()
        plugin = Youtube(None, "A test", {}, security)

        self.assertEqual(plugin.recognize("PRIVMSG", "toto", ["toto",
                                                              "https://www.youtube.com/watch?v=1H5loYi6wVc&feature=youtube_gdata_player"]),
                         True)
        self.assertEqual(plugin.data, '1H5loYi6wVc')

        self.assertEqual(
            plugin.recognize("PRIVMSG", "toto", ["toto", "https://www.youtube.com/watch?v=uNuFVq5QeRk#t=289"]), True)
        self.assertEqual(plugin.data, 'uNuFVq5QeRk')

        self.assertEqual(plugin.recognize("PRIVMSG", "toto", ["toto", "https://www.youtube.com/watch?v=203QC6hYIss"]),
                         True)
        self.assertEqual(plugin.data, '203QC6hYIss')

        self.assertEqual(
            plugin.recognize("PRIVMSG", "toto", ["toto", "titi tutu -> https://www.youtube.com/watch?v=-XyfYfuATwQ"]),
            True)
        self.assertEqual(plugin.data, '-XyfYfuATwQ')

        self.assertEqual(plugin.recognize("PRIVMSG", "toto",
                                          ["toto", "http://www.youtube.com/watch?v=0zM3nApSvMg&feature=feedrec_grec_index"]),
                         True)
        self.assertEqual(plugin.data, '0zM3nApSvMg')

        self.assertEqual(
            plugin.recognize("PRIVMSG", "toto", ["toto", "http://www.youtube.com/v/0zM3nApSvMg?fs=1&amp;hl=en_US&amp;rel=0"]),
            True)
        self.assertEqual(plugin.data, '0zM3nApSvMg')

        self.assertEqual(plugin.recognize("PRIVMSG", "toto", ["toto", "http://www.youtube.com/embed/0zM3nApSvMg?rel=0"]),
                         True)
        self.assertEqual(plugin.data, '0zM3nApSvMg')

        self.assertEqual(plugin.recognize("PRIVMSG", "toto", ["toto", "http://www.youtube.com/watch?v=0zM3nApSvMg"]),
                         True)
        self.assertEqual(plugin.data, '0zM3nApSvMg')

        self.assertEqual(plugin.recognize("PRIVMSG", "toto", ["toto", "http://youtu.be/0zM3nApSvMg"]),
                         True)
        self.assertEqual(plugin.data, '0zM3nApSvMg')