import time
import settings

# PyBot
class PyBotApplication(object):
	def __init__(self):
		self.isRunning = True
		self.startTime = time.time()
		self.settings = settings
