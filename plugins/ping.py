# -*- coding: utf8 -*-

from plugin import *


class Ping(Plugin):
    def execute(self, data):
        return 'pong'
