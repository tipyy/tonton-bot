#! /usr/bin/python
# -*- coding: utf8 -*-

import socket, string, sys, time

from pybotapplication import *
from IRCUtil import *

# Loading Application
app = PyBotApplication()

# Loading IRC connection
connection = IRCUtil.try_to_connect(app)
IRCUtil.send_messages(app.settings.channel, connection, app.settings.helloMessage)

# Starting bot
while app.isRunning:
	data = None
	data = connection.getmsg()

	print data.msg
	app.logger.info("Receive message")
	app.logger.debug(data.msg)

	for action in app.actionList:
		if action.recognize(data):
			print action.getDescription()
			result = action.execute(data)
			app.logger.info("Sending messages")
			app.logger.debug(result)
			IRCUtil.send_messages(app.settings.channel, connection, result)

connection.quit(app.settings.quitMessage)
exit()
