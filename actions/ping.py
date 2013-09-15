from action import *

class Ping(Action):
	def execute(self, data):
		return '%s:  pong' % data.by
