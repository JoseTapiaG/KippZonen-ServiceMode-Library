from Exceptions import MethodNotFound


class LogBoxSD:
    # state of LogBoxSD
    # e.g: When the LogBoxSD Receive a 's' in service mode enter in sd card setup
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

    # Interface to communicate with LogBox SD. It allows use methods of LogBoxSD
    def __init__(self, connection):
        self.connection = connection
        self.connection.connect()
        self.currentState = self.states["serviceMode"]

    def service_mode_state(self):
        self.check_state("serviceMode")
        self.connection.send('?')
        return self.connection.receive()

    def sd_mode(self):
        self.check_state("serviceMode")
        self.connection.send('s')
        response = self.connection.receive()
        if "SD CARD" in response:
            self.currentState = self.states["sdCardSetup"]
        else:
            return False
        return True

    def sd_card_state(self):
        self.check_state("sdCardSetup")
        self.connection.send('?')
        return self.connection.receive()

    def list_files(self):
        self.check_state("sdCardSetup")
        self.connection.send('l')
        return self.connection.receive()

    def type_file(self):
        self.check_state("sdCardSetup")
        self.connection.send('t')
        response = self.connection.receive()
        if "Enter the file number" in response:
            self.currentState = self.states["typingFile"]

    def get_file_data(self, file_number):
        self.check_state("typingFile")
        self.connection.send(str(file_number))
        response = self.connection.receive()
        self.currentState = self.states["sdCardSetup"]
        return response

    # check if the command can be used in the current state of LogBoxSD
    def check_state(self, state):
        if self.currentState != self.states[state]:
            raise MethodNotFound()
