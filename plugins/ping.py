# -*- coding: utf8 -*-

from core.plugin import *


class Ping(Plugin):
    def execute(self, data):
        return 'pong'
