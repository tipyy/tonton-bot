from action import *

class Quit(Action):
	def execute(self):
		self.application.isRunning = False
		return self.application.settings.quitMessage
