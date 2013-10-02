# -*- coding: utf8 -*-

from twisted.internet import reactor
from core.bot import TontonBotFactory

import logging
import settings


if __name__ == "__main__":
    # create logger
    logger = logging.getLogger("TontonBotLog")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler = logging.FileHandler(settings.logFile)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # create factory protocol and application
    factory = TontonBotFactory(settings.channel, logger)

    # connect factory to this host and port
    reactor.connectTCP(settings.server, settings.port, factory)

    # run bot
    reactor.run()
