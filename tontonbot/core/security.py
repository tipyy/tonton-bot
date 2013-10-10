class Security(object):
    def __init__(self):
        self.events = []
        self.whiteList = []
        self.blackList = []

    def addToWhiteList(self, userName):
        self.whiteList.append(userName)

    def addToBlackList(self, userName):
        self.blackList.append(userName)

    def addEvent(self, eventName):
        self.events.append(eventName)

    def checkSecurity(self, user, command):
        whiteList = (not self.whiteList) or (user in self.whiteList)
        blackList = (not self.blackList) or (user not in self.blackList)

        event = False
        if not self.events:
            event = True
        else:
            for ev in self.events:
                if command == ev:
                    event = True

        return whiteList and blackList and event
