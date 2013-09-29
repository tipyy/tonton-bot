# -*- coding: utf8 -*-

from plugin import *
from helpers import HttpHelper

import re
import unicodedata


class Dailymotion(Plugin):
    def recognize(self, user, channel, msg):

        if not self.security.checkSecurity(user, channel):
            return False

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
