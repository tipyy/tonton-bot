# -*- coding: utf8 -*-

from plugin import *

class Help(Plugin):

	def execute(self, data):
		helpString = "Listes des commandes actives pour %s:\r\n" % data.by
		for action in self.application.actionList:
			if action.command != None and action.security.checkSecurity(data):
				helpString += "%s: %s\r\n" % (action.command, action.description)
		
		return helpString
