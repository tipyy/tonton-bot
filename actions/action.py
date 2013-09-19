class Action(object):
	def __init__(self, application, command, description, security):
		self.application = application
		self.command = command
		self.description = description
		self.security = security

	def recognize(self, data):
		if (data.msg == self.command) and (self.security.checkSecurity(data)):
			self.application.logger.info("Action detected %s" % self.command)
			return True
		return False

	def execute(self, data):
		return ""
		
	def getDescription(self):
		return self.command + ": " + self.description