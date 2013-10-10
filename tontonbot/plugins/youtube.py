# -*- coding: utf8 -*-

import re
import datetime
import unicodedata

from tontonbot.core.plugin import *
from tontonbot.helpers import http_helper


class Youtube(Plugin):
    def recognize(self, command, prefix, params):
        # Checking authorizations
        Plugin.recognize(self, command, prefix, params)
        msg = irc_helper.IrcHelper.extract_message(params)

        # Checks if there is a youtube video match
        regex = '(http(s)?://)?(www.)?(youtu\.be\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v)\/))([^\?\&"\'\ >]+)'
        m = re.findall(regex, msg)
        if m:
            self.data = m[0][7]
            return True

        return False

    def execute(self, data):
        # Gets video information
        api_url = 'https://gdata.youtube.com/feeds/api/videos/%s?v=2&alt=jsonc' % self.data

        encoded_data = http_helper.HttpHelper.get_json(api_url)

        d = encoded_data['data']['duration']
        duration = str(datetime.timedelta(seconds=d))
        title = "%s / %s / %s" % (encoded_data['data']['uploader'], encoded_data['data']['title'], duration)

        # Gets user name

        return unicodedata.normalize('NFKD', title).encode('utf8', 'ignore')
