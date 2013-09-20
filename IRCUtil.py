# -*- coding: utf8 -*-

import time

from PyIC.pyic import *

class IRCUtil(object):
	@staticmethod
	def try_to_connect(app):
		connection = irc_client(app.settings.pseudo, app.settings.server, app.settings.port, False, app.settings.pseudo, app.settings.pseudo, app.settings.pseudo, None, None)
		connection.join(app.settings.channel, None)
		app.connected = True
		
		return connection

	@staticmethod		
	def send_messages(to, connection, messages):
		if messages != "":
			for line in messages.split('\r\n'):
				connection.sendmsg(to, line)
				time.sleep(1)

