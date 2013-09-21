# -*- coding: utf8 -*-

from plugin import *

class About(Plugin):
	def execute(self, data):
		return '%s: un petit bot écrit par TontonDuPirox' % data.by
