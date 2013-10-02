# -*- coding: utf8 -*-

from xml.etree import ElementTree

from core.security import *


class PluginsFactory(object):

    def create(self, config_file):
        plugin_list = []

        module = __import__("plugins")
        reload(module)

        document = ElementTree.parse(config_file)
        for pluginNode in document.findall("plugin"):
            name = pluginNode.find("name").text.encode("utf-8")
#            file = pluginNode.find("file").text.encode("utf-8")
            command = pluginNode.find("command").text.encode("utf-8")
            description = pluginNode.find("description").text.encode("utf-8")

            security = Security()
            for securityNode in pluginNode.findall("security/whitelist/user"):
                security.addToWhiteList(securityNode.text.encode("utf-8"))
            for securityNode in pluginNode.findall("security/blacklist/user"):
                security.addToBlackList(securityNode.text.encode("utf-8"))

            plugin = getattr(module, name)
            action = plugin(command, description, security)

            plugin_list.append(action)

        return plugin_list
