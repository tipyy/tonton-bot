# -*- coding: utf8 -*-


class Plugin(object):
    def __init__(self, command, description, security):
        self.command = command
        self.description = description
        self.security = security

    def recognize(self, user, channel, msg):
        if msg == self.command and self.security.checkSecurity(user, channel):
            return True
        return False

    def execute(self, data):
        return
