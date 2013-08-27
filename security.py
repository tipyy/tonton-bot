
# todo private message handling
class Security(object):
	def __init__(self):
		self.whiteList = [ ]
		self.blackList = [ ]
#		self.privateMessage = privateMessage

	def addToWhiteList(self, userName):
		self.whiteList.append(userName)

	def addToBlackList(self, userName):
		self.blackList.append(userName)
				
	def checkSecurity(self, data):
		whiteList = (not self.whiteList) or (data.by in self.whiteList)
		blackList = (not self.blackList) or (data.by not in self.blackList)
		
		return whiteList and blackList# and privateMessage and notice
