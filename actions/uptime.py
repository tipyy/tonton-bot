import time
import datetime
from action import *

class Uptime(Action):
	def execute(self, data):
		end_time = time.time()
		uptime = end_time - self.application.startTime
		uptime = str(datetime.timedelta(seconds=int(uptime)))

		return 'Uptime: ' + uptime
