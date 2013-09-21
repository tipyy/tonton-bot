# -*- coding: utf8 -*-

from security import *
import plugins
from xml.etree import ElementTree

class PluginsFactory(object):

	def create(self, application):
		actionList = []

		document = ElementTree.parse("plugins/settings.xml")
		for pluginNode in document.findall("plugin"):
			name = pluginNode.find("name").text
			command = pluginNode.find("command").text
			description = pluginNode.find("description").text.encode("utf-8")
    
			security = Security()
			for securityNode in pluginNode.findall("security/whitelist/user"):
				security.addToWhiteList(securityNode.text.encode("utf-8"))
			
			plugin = eval("plugins.%s" % name)(application, command, description, security)
			actionList.append(plugin)
		
		return actionList
