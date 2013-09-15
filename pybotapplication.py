import time
import settings
from actionListFactory import *

# PyBot
class PyBotApplication(object):
	def __init__(self):
		self.isRunning = True
		self.startTime = time.time()
		self.settings = settings
		self.actionList = ActionListFactory().create(self)
