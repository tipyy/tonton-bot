# -*- coding: utf8 -*-

import unicodedata

from tontonbot.core.plugin import *
from tontonbot.helpers import http_helper


class LastFM(Plugin):
    def recognize(self, command, prefix, params):
        # Checking authorizations
        Plugin.recognize(self, command, prefix, params)
        msg = irc_helper.IrcHelper.extract_message(params)

        if msg.startswith(self.command):
            self.data = msg.split(" ")
            return True

        return False

    def execute(self, data):
        if len(self.data) > 1:
            user = self.data[1]

            api_url = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=%s&api_key=%s&format=json' % (user, self.config["api_key"])
            encoded_data = http_helper.HttpHelper.get_json(api_url)
            most_recent = encoded_data["recenttracks"]["track"][0]

            title = "Derniere chanson ecoutee par %s : %s - %s" % (user, most_recent["artist"]["#text"], most_recent["name"])
            if "@attr" in most_recent and 'nowplaying' in most_recent["@attr"] and most_recent["@attr"]['nowplaying'] == "true":
                title = "%s ecoute actuellement : %s - %s" % (user, most_recent["artist"]["#text"], most_recent["name"])

            return unicodedata.normalize('NFKD', title).encode('utf8', 'ignore')
        else:
            return "Usage: !%s username" % self.command
