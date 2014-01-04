# -*- coding: utf8 -*-

from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
from twisted.python import log
from tontonbot import settings
from tontonbot.core.plugin_list_manager import PluginListManager
from tontonbot.helpers import irc_helper


class TontonBot(irc.IRCClient):
    """The IRC bot himself"""
    def __init__(self, channel):
        """Constructor setting nickname and plugin list"""
        self.nickname = settings.nickname
        self.channel = channel
        self.plugins_manager = None
        self.connected = False
        try:
            self.plugins_manager = PluginListManager(settings.pluginConfigFile)
        except:
            log.err()

    def signedOn(self):
        """Called when bot has successfully signed on to server."""
        self.join(self.channel)
        self.connected = True

    def handleCommand(self, command, prefix, params):
        """
        from super class
        """
        if self.connected is True:
            try:
                msg = irc_helper.IrcHelper.extract_message(params)
                user = irc_helper.IrcHelper.extract_nickname(prefix)
                channel = irc_helper.IrcHelper.extract_sender(user, params[0], settings.nickname)

                log.msg("Message from %s to %s : %s" % (user, channel, msg))

                result = self.plugins_manager.parseMessage(command, prefix, params)
                self.sendMessage(channel, result)

                if (channel == self.nickname or msg.startswith(self.nickname + ":")) and user != settings.owner and user != self.nickname:
                    self.sendMessage(channel, "Désolé je ne suis qu'un bot, et je ne parle pas aux inconnus.")
                    return

                if msg == "!reload" and user == settings.owner:
                    self.plugins_manager.reloadPlugins()
                    self.sendMessage(channel, "plugins rechargés.")

                if msg == "!quit" and user == settings.owner:
                    self.factory.running = False
                    self.sendMessage(channel, settings.quitMessage)
                    self.quit(settings.quitMessage)
                if msg == "!help" and user == settings.owner:
                    self.sendMessage(channel, self.plugins_manager.pluginsHelp())
            except:
                log.err()
        irc.IRCClient.handleCommand(self, command, prefix, params)

    def sendMessage(self, channel, msg):
        if msg != "" and msg is not None:
            for line in msg.split("\r\n"):
                log.msg("Sending message to %s : %s" % (channel, line))
                self.msg(channel, line)

class TontonBotFactory(protocol.ClientFactory):
    """
    A factory for TontonBots.
    A new protocol instance will be created each time we connect to the server.
    """
    def __init__(self, channel):
        self.channel = channel
        self.running = True
        log.startLogging(open(settings.logFile, "w"))

    def buildProtocol(self, addr):
        p = TontonBot(self.channel)
        p.factory = self
        return p

    def clientConnectionLost(self, connector, reason):
        """If we get disconnected, reconnect to server."""
        if self.running:
            log.err("reconnecting...")
            connector.connect()
        else:
            reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        """On connection failed"""
        log.err("connection failed.")
        reactor.stop()

