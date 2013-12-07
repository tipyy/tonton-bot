# -*- coding: utf8 -*-

import re
import datetime
import unicodedata

from tontonbot.core.plugin import *
from tontonbot.helpers import HttpHelper
from tontonbot.helpers import IrcHelper


class Youtube(Plugin):
    def recognize(self, command, prefix, params):
        # Checking authorizations
        Plugin.recognize(self, command, prefix, params)
        msg = IrcHelper.extract_message(params)

        # Checks if there is a youtube video match
        regex = '(http(s)?://)?(www.)?(youtu\.be\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v)\/))([^\?\&"\'\#\ >]+)'
        m = re.findall(regex, msg)
        if m:
            self.data = m[0][7]
            return True

        return False

    def execute(self, data):
        # Gets video information
        api_url = 'https://gdata.youtube.com/feeds/api/videos/%s?v=2&alt=json' % self.data
        encoded_data = HttpHelper.get_json(api_url)

        # Gets the infos from json
        d = int(encoded_data['entry']['media$group']['yt$duration']['seconds'])
        duration = str(datetime.timedelta(seconds=d))
        author = encoded_data['entry']['author'][0]['name']['$t']
        vid_title = encoded_data['entry']['title']['$t']
        # Build return string
        title = "%s / %s / %s" % (author, vid_title, duration)

        return unicodedata.normalize('NFKD', title).encode('utf8', 'ignore')
