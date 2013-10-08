# -*- coding: utf8 -*-

from xml.etree import ElementTree
from core.security import *

import re


class PluginsFactory(object):

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

    def create(self, config_file):
        """
        Creates the plugin list from xml config_file
        """
        plugin_list = []

        document = ElementTree.parse(config_file)
        for pluginNode in document.findall("plugin"):
            name = pluginNode.find("name").text.encode("utf-8")
            fileName = pluginNode.find("file").text.encode("utf-8")
            command = pluginNode.find("command").text.encode("utf-8")
            description = pluginNode.find("description").text.encode("utf-8")

            security = Security()
            for securityNode in pluginNode.findall("security/whitelist/user"):
                security.addToWhiteList(securityNode.text.encode("utf-8"))
            for securityNode in pluginNode.findall("security/blacklist/user"):
                security.addToBlackList(securityNode.text.encode("utf-8"))

            plugin = self.reimport("plugins.%s.%s" % (fileName, name))
            action = plugin(command, description, security)

            plugin_list.append(action)

        return plugin_list
