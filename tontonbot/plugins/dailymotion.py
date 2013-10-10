# -*- coding: utf8 -*-

import re
import unicodedata

from tontonbot.core.plugin import *
from tontonbot.helpers import HttpHelper


class Dailymotion(Plugin):
    def recognize(self, command, prefix, params):
        # Checking authorizations
        Plugin.recognize(self, command, prefix, params)
        msg = irc_helper.IrcHelper.extract_message(params)

        # Searching for regex
        regex = '(https?://)?(www.)?dailymotion.com\/((video|hub)\/)([a-zA-Z0-9]+)([\?\&"\'\ >_]?)'
        m = re.findall(regex, msg)
        if m:
            self.data = m[0][4]
            return True

        return False

    def execute(self, data):
        api_url = 'https://api.dailymotion.com/video/%s' % self.data
        encoded_data = HttpHelper.get_json(api_url)

        return unicodedata.normalize('NFKD', encoded_data['title']).encode('utf8', 'ignore')
