class Security(object):
    def __init__(self):
        self.event_list = []
        self.white_list = []
        self.black_list = []

    def addToWhiteList(self, userName):
        self.white_list.append(userName)

    def addToBlackList(self, userName):
        self.black_list.append(userName)

    def addEvent(self, eventName):
        self.event_list.append(eventName)

    def checkSecurity(self, user, command):
        whiteList = (not self.white_list) or (user in self.white_list)
        blackList = (not self.black_list) or (user not in self.black_list)

        event = False
        if not self.event_list:
            event = True
        else:
            for ev in self.event_list:
                if command == ev:
                    event = True

        return whiteList and blackList and event
