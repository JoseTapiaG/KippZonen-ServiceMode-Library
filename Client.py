from Data import Data
from MySocket import MySocket


class Client:

    def __init__(self, host = "", port = ""):
        if not "".__eq__(host) or not "".__eq__(port):
            self.mySocket = MySocket()
            self.mySocket.connect(host, port)

    def getDayData(self, date):

        if not self.connectLogBox():
            return "ERROR"

        if not self.connectSD():
            return "ERROR"

        fileNumber = self.getFileNumber(date)
        if fileNumber != -1 :
            data = self.getDataWithFileNumber(fileNumber)

        self.mySocket.mySendAndReceive("c\n")
        return data


    def connectLogBox(self):
        for x in range(3):
            response = self.mySocket.mySendAndReceive("\x03\n")
            if "Service mode started" in response:
                return True
            return False


    def connectSD(self):
        for x in range(3):
            response = self.mySocket.mySendAndReceive("s\n")
            # todo falta chequear
            if "SD CARD" in response:
                return True
            return False

    #ejemplo de registro: "ELOG0000.TXT  51 2007-06-16 13:21:06"
    def getFileNumber(self, date):
        for x in range(3):
            response = self.mySocket.mySendAndReceive("l\n")

            if "SD card size:" in response:
                for fileName in self.splitFileNames(response):
                    if date == self.getDateOfFileName(fileName):
                        return self.getFileNumberOfFileName(fileName)
        return -1

    def splitFileNames(self, str):
        return str.split("\n")

    def getDateOfFileName(self, str):

        if "SD card size:" in str:
            return -1
        split = str.split(" ")
        return split[3]

    def getFileNumberOfFileName(self, str):
        return int(str.split(" ")[0][4:-4])

    def getDataWithFileNumber(self, fileNumber):
        for x in range(3):
            enterFileNumber = False
            for x in range(3):
                if "Enter the file number" in self.mySocket.mySendAndReceive("t\n") :
                    enterFileNumber = True
                    break

            if enterFileNumber :
                for x in range(3):
                    response = self.mySocket.mySendAndReceive(str(fileNumber) + "\n")
                    if "File#" in response:
                        registers = []
                        for register in response.split("\n"):
                            split = register.split(" ")
                            if len(split) == 14:
                                registers.append(self.parseRegister(split))
                        if registers:
                            return registers

    #ejemplo de registro: "2015-12-13 23:50:03  0.011   0.079   0.252 / / / / / / / /"
    def parseRegister(self, split):
        data = Data(
            date = split[0],
            time = split[1],
            data1 = split[3],
            data2 = split[6],
            data3 = split[9]
        )

        return data