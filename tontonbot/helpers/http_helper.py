# -*- coding: utf8 -*-
import urllib2
import json


class HttpHelper(object):
    @staticmethod
    def get_json(url):
        req = urllib2.Request(url, headers={'User-Agent': "Tonton bot"})
        con = urllib2.urlopen(req)
        json_encoded = con.read()
        encoded_data = json.loads(json_encoded)

        return encoded_data
