# -*- coding: utf8 -*-

import re
import urllib2

from tontonbot.core.plugin import *
from tontonbot.helpers import IrcHelper


class HttpError(Plugin):
    def recognize(self, command, prefix, params):
        # Checking authorizations
        Plugin.recognize(self, command, prefix, params)
        msg = IrcHelper.extract_message(params)

        # Searching for regex
        # @see https://gist.github.com/uogbuji/705383
        regex = re.compile(
            ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:'
            ur'[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)'
            ur'|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')

        m = re.findall(regex, msg)
        if not m:
            return False
        self.data = m[0][0]

        return True

    def execute(self, data):
        message = None

        try:
            req = urllib2.Request(self.data, headers={'User-Agent': "Tonton bot"})
            con = urllib2.urlopen(req)
            con.read()
        except urllib2.HTTPError, e:
            message = "%s retourne une erreur %s" % (self.data, e.code)
        except urllib2.URLError, e:
            message = "je n'ai pas pu attendre l'url %s : %s" % (self.data, e.reason)
        except ValueError:
            return

        return message
