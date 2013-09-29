# -*- coding: utf8 -*-


class IrcHelper(object):
    @staticmethod
    def extract_nickname(nickname):
        source = nickname
        tmp = nickname.split("!")
        if len(tmp) > 1:
            source = tmp[0]

        return source
