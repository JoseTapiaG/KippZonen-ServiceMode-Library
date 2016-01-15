from Exceptions import MethodNotFound

class LogBoxSD:
    states = {

        "serviceMode": {
            '?': "serviceModeState",
            's': "sdMode"
        },

        "sdCardSetup": {
            '?': "sdCardState",
            'l': "listFiles",
            't': "typeFile"
        },

        "typingFile": {
            'n': "getFileData"
        }

    }

    def __init__(self, connection):
        self.connection = connection
        self.connection.connect()
        self.currentState = self.states["serviceMode"]

    def serviceModeState(self):
        self.checkState("serviceMode")
        self.connection.send('?')
        return self.connection.receive()


    def sdMode(self):
        self.checkState("serviceMode")
        self.connection.send('s')
        response = self.connection.receive()
        if "SD CARD" in response:
            self.currentState = self.states["sdCardSetup"]
        else:
            return False
        return True


    def sdCardState(self):
        self.checkState("sdCardSetup")
        self.connection.send('?')
        return self.connection.receive()


    def listFiles(self):
        self.checkState("sdCardSetup")
        self.connection.send('l')
        return self.connection.receive()


    def typeFile(self):
        self.checkState("sdCardSetup")
        self.connection.send('t')
        response = self.connection.receive()
        if "Enter the file number" in response:
            self.currentState = self.states["typingFile"]

    def getFileData(self, fileNumber):
        self.checkState("typingFile")
        self.connection.send(str(fileNumber))
        response = self.connection.receive()
        self.currentState = self.states["sdCardSetup"]
        return response

    def checkState(self, state):
        if self.currentState != self.states[state]:
            raise MethodNotFound('Method not found')