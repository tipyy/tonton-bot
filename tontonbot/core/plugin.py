# -*- coding: utf8 -*-

from tontonbot.helpers import irc_helper


class Plugin(object):
    def __init__(self, name, command, description, config, security):
        self.name = name
        self.data = None
        self.config = config
        self.command = command
        self.description = description
        self.security = security

    def recognize(self, command, prefix, params):
        self.data = None

        user = irc_helper.IrcHelper.extract_nickname(prefix)
        msg = irc_helper.IrcHelper.extract_message(params)

        if (msg == self.command or self.command is None) and self.security.checkSecurity(user, command):
            return True
        return False

    def execute(self, data):
        pass
