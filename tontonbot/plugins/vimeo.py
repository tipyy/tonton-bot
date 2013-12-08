# -*- coding: utf8 -*-

import re
import datetime
import unicodedata

from tontonbot.core.plugin import *
from tontonbot.helpers import HttpHelper
from tontonbot.helpers import IrcHelper


class Vimeo(Plugin):
    def recognize(self, command, prefix, params):
        # Checking authorizations
        Plugin.recognize(self, command, prefix, params)
        msg = IrcHelper.extract_message(params)

        # Checks if there is a youtube video match
        regex = '(http(s)?://)?(www.)?vimeo\.com/(\w*/)*(\d+)'
        m = re.findall(regex, msg)
        if m:
            self.data = m[0][4]
            return True

        return False

    def execute(self, data):
        # Gets video information
        api_url = 'http://vimeo.com/api/v2/video/%s.json' % self.data
        encoded_data = HttpHelper.get_json(api_url)
        d = encoded_data[0]['duration']
        duration = str(datetime.timedelta(seconds=d))
        title = "%s / %s / %s" % (encoded_data[0]['user_name'], encoded_data[0]['title'], duration)

        return unicodedata.normalize('NFKD', title).encode('utf8', 'ignore')
