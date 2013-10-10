# -*- coding: utf8 -*-

import re
import urllib2

from bs4 import BeautifulSoup

from core.plugin import *


class NSFWGag(Plugin):
    def recognize(self, command, prefix, params):
        # Checking authorizations
        Plugin.recognize(self, command, prefix, params)
        msg = irc_helper.IrcHelper.extract_message(params)

        # Searching for regex
        regex = '((http://|https://)*(www.)*9gag.com[a-zA-Z/0-9?=]*)'
        m = re.findall(regex, msg)
        if m:
            try:
                url = urllib2.urlopen('%s' % m[0][0]).read()
            except urllib2.HTTPError:
                pass

            soup = BeautifulSoup(url)
            if soup.find('p', {'class': 'form-message error '}) is not None:
                self.data = 'Ce post a été supprimé'
                return True

            if soup.find('div', {'class': 'nsfw-post'}) is not None:
                self.data = 'Ce post de 9gag nécessite de s\'identidier'
                return True

        return False

    def execute(self, data):
        return self.data
