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
        self.plugins_manager = []
        try:
            self.plugins_manager = PluginListManager(settings.pluginConfigFile)
        except:
            log.err()

    def signedOn(self):
        """Called when bot has successfully signed on to server."""
        self.join(self.channel)

    def handleCommand(self, command, prefix, params):
        """
        from super class
        """
        try:
            result = self.plugins_manager.parseMessage(command, prefix, params)
            channel = irc_helper.IrcHelper.extract_sender(prefix, params[0], settings.nickname)
            self.sendMessage(channel, result)
        except:
            log.err()

        irc.IRCClient.handleCommand(self, command, prefix, params)

    def sendMessage(self, channel, msg):
        if msg != "" and msg is not None:
            for line in msg.split("\r\n"):
                log.msg("Sending message to %s : %s" % (channel, line))
                self.msg(channel, line)

    def privmsg(self, user, channel, msg):
        """This will get called when the bot receives a message."""
        user = irc_helper.IrcHelper.extract_nickname(user)
        channel = irc_helper.IrcHelper.extract_sender(user, channel, settings.nickname)
        log.msg("message from %s to %s : %s" % (user, channel, msg))

        if (channel == self.nickname or msg.startswith(self.nickname + ":")) and user != settings.owner and user != self.nickname:
            self.sendMessage(channel, "Désolé je ne suis qu'un bot, et je ne parle pas aux inconnus.")
            return

        if msg == "!reload" and user == settings.owner:
            try:
                self.plugins_manager.reloadPlugins()
                self.sendMessage(channel, "plugins rechargés.")
            except:
                log.err()

        if msg == "!quit" and user == settings.owner:
            self.factory.running = False
            self.sendMessage(channel, settings.quitMessage)
            self.quit(settings.quitMessage)


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

