from plugin import *

class Quit(Plugin):
	def execute(self, data):
		self.application.isRunning = False
		return self.application.settings.quitMessage
