class Action(object):
	def __init__(self, application, command, description, security):
		self.application = application
		self.command = command
		self.description = description
		self.security = security
				
	def recognize(self, data):
		ok = (data.msg == self.command) and (self.security.checkSecurity(data))

		return ok

	def execute(self):
		return ""
		
	def getDescription(self):
		return self.command + ": " + self.description