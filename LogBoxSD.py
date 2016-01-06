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

    def __init__(self, conexion):
        self.conexion = conexion
        self.conexion.connect
        self.currentState = self.states["serviceMode"]

    def serviceModeState(self):
        self.checkState("serviceMode")
        self.conexion.send('?')
        return self.conexion.receive()


    def sdMode(self):
        self.checkState("serviceMode")
        self.conexion.send('s')
        response = self.conexion.receive
        if "SD CARD" in response:
            self.currentState = self.states["sdCardSetup"]
        else:
            return False
        return True


    def sdCardState(self):
        self.checkState("sdCardSetup")
        self.conexion.send('?')
        return self.conexion.receive()


    def listFiles(self):
        self.checkState("sdCardSetup")
        self.conexion.send('l')
        return self.conexion.receive()


    def typeFile(self):
        self.checkState("sdCardSetup")
        self.conexion.send('t')
        response = self.conexion.receive()
        if "Enter the file number" in response:
            self.currentState = self.states["typingFile"]

    def getFileData(self, fileNumber):
        self.checkState("typingFile")
        self.conexion.send('t')
        response = self.conexion.receive()
        self.currentState = self.states["sdCardSetup"]
        return response

    def checkState(self, state):
        if self.currentState == self.states[state]:
            raise MethodNotFound('Method not found')
