import time, logging
import settings
from actionListFactory import *

# PyBot
class PyBotApplication(object):
	def __init__(self):
		self.isRunning = True
		self.connected = False
		self.startTime = time.time()
		self.settings = settings
		self.actionList = ActionListFactory().create(self)
		
		# Enabling logger
		self.logger = logging.getLogger("TontonBotLog")
		self.logger.setLevel(logging.DEBUG)
		formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
		handler = logging.FileHandler(settings.logFile)
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)

