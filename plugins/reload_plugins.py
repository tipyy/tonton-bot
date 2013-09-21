# -*- coding: utf8 -*-

from plugin import *

class ReloadPlugins(Plugin):

	def execute(self, data):
		self.application.reloadActionList()
		return "Plugins rechargés"
