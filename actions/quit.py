from action import *

class Quit(Action):
	def execute(self, data):
		self.application.isRunning = False
		return self.application.settings.quitMessage
