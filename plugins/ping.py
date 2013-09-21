from plugin import *

class Ping(Plugin):
	def execute(self, data):
		return '%s: pong' % data.by
