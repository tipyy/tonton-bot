# -*- coding: utf8 -*-

from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
from pluginsFactory import PluginsFactory
from helpers import irc_helper, exception_helper

import settings


class TontonBot(irc.IRCClient):
    """The IRC bot himself"""
    def __init__(self, channel):
        """Constructor setting nickname and plugin list"""
        self.nickname = settings.nickname
        self.plugin_list = PluginsFactory().create(settings.pluginConfigFile)
        self.channel = channel

    def reloadPlugins(self):
        """Reloading plugins configuration"""
        self.plugin_list = PluginsFactory().create(settings.pluginConfigFile)

    def connectionMade(self):
        """On connection made we call parent function"""
        irc.IRCClient.connectionMade(self)
        self.factory.logger.info("Connected to server")

    def connectionLost(self, reason):
        """On connection lost we call parent function"""
        self.factory.logger.info("Disconnected from server")
        irc.IRCClient.connectionLost(self, reason)

    # callbacks for events

    def signedOn(self):
        """Called when bot has succesfully signed on to server."""
        self.join(self.channel)

    def joined(self, channel):
        """This will get called when the bot joins the channel."""
        self.factory.logger.info("Connected to chan %s" % self.factory.channel)
        self.msg(channel, settings.helloMessage)

    def privmsg(self, user, channel, msg):
        """This will get called when the bot receives a message."""
        user = irc_helper.IrcHelper.extract_nickname(user)
        self.factory.logger.info("message from %s to %s : %s" % (user, channel, msg))

        if (channel == self.nickname or msg.startswith(self.nickname + ":")) and user != settings.owner:
            msg = "Désolé je ne suis qu'un bot, et je ne parle pas aux inconnus."
            self.msg(user, msg)
            return

        if msg == "!reload" and user == settings.owner:
            self.factory.logger.info("Reload plugins.")
            self.msg(user, "plugins rechargés.")
            self.reloadPlugins()

        if msg == "!quit" and user == settings.owner:
            self.factory.logger.info("Good bye.")
            self.factory.running = False
            self.msg(channel, settings.quitMessage)
            self.quit(settings.quitMessage)

        for action in self.plugin_list:
            try:
                if action.recognize(user, channel, msg):
                    self.factory.logger.info("Action detected %s" % action.command)
                    result = action.execute(msg)
                    if result != "" and result is not None:
                        for line in result.split("\r\n"):
                            self.factory.logger.info("Sending message to %s : %s" % (channel, line))
                            self.msg(channel, line)
            except Exception:
                exception_helper.ExceptionHelper.write_traceback('Error on plugin %s' % action.command, logger)


class TontonBotFactory(protocol.ClientFactory):
    """
    A factory for TontonBots.
    A new protocol instance will be created each time we connect to the server.
    """

    def __init__(self, channel, logger):
        self.channel = channel
        self.logger = logger
        self.running = True

    def buildProtocol(self, addr):
        p = TontonBot(self.channel)
        p.factory = self
        return p

    def clientConnectionLost(self, connector, reason):
        """If we get disconnected, reconnect to server."""
        if self.running:
            self.logger.error("reconnecting...")
            connector.connect()

    def clientConnectionFailed(self, connector, reason):
        self.logger.error("connection failed.")
        reactor.stop()

