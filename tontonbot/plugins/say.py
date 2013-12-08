# -*- coding: utf8 -*-

from tontonbot.core.plugin import Plugin


class Say(Plugin):
    def execute(self, data):
        return self.config["message"]
