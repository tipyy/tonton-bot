# -*- coding: utf8 -*-

from twisted.internet import reactor
from core.bot import TontonBotFactory

import settings


if __name__ == "__main__":
    # create factory protocol and application
    factory = TontonBotFactory(settings.channel)

    # connect factory to this host and port
    reactor.connectTCP(settings.server, settings.port, factory)

    # run bot
    reactor.run()
