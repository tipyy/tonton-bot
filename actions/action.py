class Action(object):
	def __init__(self, application, command, description, security):
		self.application = application
		self.command = command
		self.description = description
		self.security = security
				
	def recognize(self, data):
		return (data.msg == self.command) and (self.security.checkSecurity(data))

	def execute(self, data):
		return ""
		
	def getDescription(self):
		return self.command + ": " + self.description