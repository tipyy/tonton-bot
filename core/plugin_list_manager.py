# -*- coding: utf8 -*-

from xml.etree import ElementTree
from core.security import *

import re


class PluginListManager(object):
    def __init__(self, config_file):
        """Constructor setting nickname and plugin list"""
        self.config_file = config_file
        self.plugin_list = None
        self.create()

    def reloadPlugins(self):
        """Reloading plugins configuration"""
        self.create()

    def create(self):
        """
        Creates the plugin list from xml config_file
        """
        self.plugin_list = []

        document = ElementTree.parse(self.config_file)
        for pluginNode in document.findall("plugin"):
            name = pluginNode.find("name").text.encode("utf-8")
            file_name = pluginNode.find("file").text.encode("utf-8")
            command = None
            if pluginNode.find("command") is not None:
                command = pluginNode.find("command").text.encode("utf-8")
            description = pluginNode.find("description").text.encode("utf-8")

            security = Security()
            for securityNode in pluginNode.findall("security/whitelist/user"):
                security.addToWhiteList(securityNode.text.encode("utf-8"))
            for securityNode in pluginNode.findall("security/blacklist/user"):
                security.addToBlackList(securityNode.text.encode("utf-8"))

            plugin = self.reimport("plugins.%s.%s" % (file_name, name))
            action = plugin(command, description, security)
            self.plugin_list.append(action)

    def parseMessage(self, user, channel, msg):
        result = ""

        for action in self.plugin_list:
            if action.recognize(user, channel, msg):
                result = action.execute(msg)

        return result


    def reimport(self, full_path):
        """
        Reload and reimport class.  Return the new definition of the class.
        @see http://stackoverflow.com/questions/9645388/dynamically-reload-a-class-definition-in-python
        """
        # Naively parse the module name and class name.
        # Can be done much better...
        match = re.match(r'(.*)\.([^\.]+)', full_path)
        module_name = match.group(1)
        class_name = match.group(2)

        # This is where the good stuff happens.
        mod = __import__(module_name, fromlist=[class_name])
        reload(mod)

        # The (reloaded definition of the) class itself is returned.
        return getattr(mod, class_name)
