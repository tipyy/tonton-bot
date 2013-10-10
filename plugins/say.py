# -*- coding: utf8 -*-

from core.plugin import *


class Say(Plugin):
    def execute(self, data):
        return self.config["message"]
