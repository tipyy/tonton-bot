# -*- coding: utf8 -*-

from action import *

class About(Action):
	def execute(self, data):
		return '%s: un petit bot écrit par TontonDuPirox' % data.by
