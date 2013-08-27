#! /usr/bin/python
# -*- coding: utf8 -*-

import socket, string, sys

from pybotapplication import *
from actionListFactory import *
from irclib.ircclient import *

from PyIC.pyic import *

# Loading Application
app = PyBotApplication()

# todo : put connection in app
# Loading IRC connection
connection = irc_client(app.settings.pseudo, app.settings.server, app.settings.port, False, app.settings.pseudo, app.settings.pseudo, app.settings.pseudo, None, None)
connection.join(app.settings.channel, None)
connection.sendmsg(app.settings.channel, app.settings.helloMessage)

# Loading action list
actionList = ActionListFactory().create(app)

# Starting bot
while app.isRunning:
    data = connection.getmsg()
       
    for action in actionList:
    	if action.recognize(data):
			result = action.execute()
			for line in result.split('\r\n'):
				connection.sendmsg(app.settings.channel, line)

	if data.msg == '!help':
		connection.sendmsg(app.settings.channel, "Listes des commandes actives :")		
		for action in actionList:
			if action.command != None and action.security.checkSecurity(data):
				connection.sendmsg(app.settings.channel, action.getDescription())
 
#    print data.msg

connection.quit(app.settings.quitMessage)
exit()
