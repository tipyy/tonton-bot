#! /usr/bin/python
# -*- coding: utf8 -*-

import socket, string, sys, time

from pybotapplication import *
from irclib.ircclient import *

from PyIC.pyic import *

# Loading Application
app = PyBotApplication()

# Util function
def send_messages(messages):
	app.logger.info("Send messages")
	app.logger.debug(messages)  
	if messages != "":
		for line in messages.split('\r\n'):
			connection.sendmsg(app.settings.channel, line)
			time.sleep(1)

# Loading IRC connection
connection = irc_client(app.settings.pseudo, app.settings.server, app.settings.port, False, app.settings.pseudo, app.settings.pseudo, app.settings.pseudo, None, None)
connection.join(app.settings.channel, None)
app.connected = True
send_messages(app.settings.helloMessage)

# Starting bot
while app.isRunning:
	data = None
	data = connection.getmsg()

	print data.msg

	for action in app.actionList:
		if action.recognize(data):
			print action.getDescription()
			result = action.execute(data)
			send_messages(result)

connection.quit(app.settings.quitMessage)
exit()
