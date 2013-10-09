# -*- coding: utf8 -*-

from plugin import *
from helpers import http_helper

import unicodedata


class LastFM(Plugin):
    def recognize(self, user, channel, msg):
        # Checks plugin authorization
        if not self.security.checkSecurity(user, channel):
            return False

        if msg.startswith(self.command):
            self.data = msg.split(" ")
            return True

        return False

    def execute(self, data):
        if len(self.data) > 1:
            user = self.data[1]

            api_url = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=%s&api_key=98cba0b8b4b0a760145aff684a2f83c2&format=json' % user
            encoded_data = http_helper.HttpHelper.get_json(api_url)
            most_recent = encoded_data["recenttracks"]["track"][0]

            title = "Derniere chanson ecoutee par %s : %s - %s" % (user, most_recent["artist"]["#text"], most_recent["name"])
            if "@attr" in most_recent and 'nowplaying' in most_recent["@attr"] and most_recent["@attr"]['nowplaying'] == "true":
                title = "%s ecoute actuellement : %s - %s" % (user, most_recent["artist"]["#text"], most_recent["name"])

            return unicodedata.normalize('NFKD', title).encode('utf8', 'ignore')
        else:
            return "Usage: !%s username" % self.command
