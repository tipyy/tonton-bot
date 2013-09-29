# -*- coding: utf8 -*-

from plugin import *

import re
import urllib2


class HttpError(Plugin):
    def recognize(self, user, channel, msg):
        if not self.security.checkSecurity(user, channel):
            return False

        # @see https://gist.github.com/uogbuji/705383
        regex = re.compile(
            ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:'
            ur'[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)'
            ur'|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')

        m = re.findall(regex, msg)

        if not m:
            return False
        url = m[0][0]

        try:
            req = urllib2.Request(url, headers={'User-Agent': "Tonton bot"})
            con = urllib2.urlopen(req)
            con.read()

            return False
        except urllib2.HTTPError, e:
            self.data = "%s retourne une erreur %s" % (url, e.code)
        except urllib2.URLError, e:
            self.data = "je n'ai pas pu attendre l'url %s : %s" % (url, e.reason)
        except ValueError, e:
            return False

        return True

    def execute(self, data):
        return self.data
