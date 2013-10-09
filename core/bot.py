# -*- coding: utf8 -*-

from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
from twisted.python import log
from core.pluginsFactory import PluginsFactory
from helpers import irc_helper

import settings


class TontonBot(irc.IRCClient):
    """The IRC bot himself"""
    def __init__(self, channel):
        """Constructor setting nickname and plugin list"""
        self.nickname = settings.nickname
        self.plugin_list = None
        self.reloadPlugins()
        self.channel = channel

    def reloadPlugins(self):
        """Reloading plugins configuration"""
        try:
            self.plugin_list = PluginsFactory().create(settings.pluginConfigFile)
        except:
            log.err()

    def connectionMade(self):
        """On connection made we call parent function"""
        irc.IRCClient.connectionMade(self)
        log.msg("Connected to server")

    def connectionLost(self, reason):
        """On connection lost we call parent function"""
        log.msg("Disconnected from server")
        irc.IRCClient.connectionLost(self, reason)

    # callbacks for events

    def signedOn(self):
        """Called when bot has successfully signed on to server."""
        self.join(self.channel)

    def joined(self, channel):
        """This will get called when the bot joins the channel."""
        log.msg("Connected to chan %s" % channel)
        self.msg(channel, settings.helloMessage)

    def privmsg(self, user, channel, msg):
        """This will get called when the bot receives a message."""
        user = irc_helper.IrcHelper.extract_nickname(user)
        log.msg("message from %s to %s : %s" % (user, channel, msg))

        if (channel == self.nickname or msg.startswith(self.nickname + ":")) and user != settings.owner and user != self.nickname:
            msg = "Désolé je ne suis qu'un bot, et je ne parle pas aux inconnus."
            self.msg(user, msg)
            return

        if msg == "!reload" and user == settings.owner:
            log.msg("Reload plugins.")
            self.msg(user, "plugins rechargés.")
            self.reloadPlugins()

        if msg == "!quit" and user == settings.owner:
            log.msg("Good bye.")
            self.factory.running = False
            self.msg(channel, settings.quitMessage)
            self.quit(settings.quitMessage)

        for action in self.plugin_list:
            try:
                if action.recognize(user, channel, msg):
                    log.msg("Action detected %s" % action.command)
                    result = action.execute(msg)
                    if result != "" and result is not None:
                        for line in result.split("\r\n"):
                            log.msg("Sending message to %s : %s" % (channel, line))
                            self.msg(channel, line)
            except:
                log.err()


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

    def clientConnectionFailed(self, connector, reason):
        """On connection failed"""
        log.err("connection failed.")
        reactor.stop()

