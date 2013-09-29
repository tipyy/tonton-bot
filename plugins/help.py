# -*- coding: utf8 -*-

from plugin import *

class Help(Plugin):

	def execute(self, data):
		source = data.source
		tmp = data.source.split("!")
		if len(tmp) > 1:
			source = tmp[0]

		helpString = u"Listes des commandes actives pour %s:\r\n" % source
		for action in self.application.actionList:
			if action.command != None and action.security.checkSecurity(data):
				helpString += u"%s: %s\r\n" % (action.command, action.description)
		
		return helpString
