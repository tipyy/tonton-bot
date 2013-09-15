# -*- coding: utf8 -*-

from action import *

class Help(Action):

	def execute(self, data):
		helpString = "Listes des commandes actives pour %s:\r\n" % data.by
		for action in self.application.actionList:
			if action.command != None and action.security.checkSecurity(data):
				helpString += action.getDescription() + '\r\n'
		
		return helpString
