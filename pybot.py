#! /usr/bin/python
# -*- coding: utf8 -*-

import socket, string, sys, time

from pybotapplication import *
from irclib.ircclient import *

from PyIC.pyic import *

# Loading Application
app = PyBotApplication()

# Loading IRC connection
connection = irc_client(app.settings.pseudo, app.settings.server, app.settings.port, False, app.settings.pseudo, app.settings.pseudo, app.settings.pseudo, None, None)
connection.join(app.settings.channel, None)
connection.sendmsg(app.settings.channel, app.settings.helloMessage)

def send_messages(messages):
	if messages != "":
		for line in messages.split('\r\n'):
			connection.sendmsg(app.settings.channel, line)
			time.sleep(2)

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

#	if data.msg == '!help' and data.by != app.settings.pseudo:
#		messages = "Listes des commandes actives pour \r\n"
#		for action in actionList:
#			if action.command != None and action.security.checkSecurity(data):
#				messages += "%s\r\n" % action.getDescription()
#		send_messages(messages)

connection.quit(app.settings.quitMessage)
exit()
