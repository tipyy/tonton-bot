# -*- coding: utf8 -*-


class IrcHelper(object):
    @staticmethod
    def extract_nickname(nickname):
        source = nickname
        tmp = nickname.split("!")
        if len(tmp) > 1:
            source = tmp[0]

        return source

    @staticmethod
    def extract_sender(user, channel, me):
        sender = channel
        if channel == me:
            sender = user

        return sender
