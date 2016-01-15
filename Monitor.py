from Data import Data
from LogBoxSD import LogBoxSD
import MyRequest

class Monitor:
    def __init__(self, connection):
        self.logBoxSD = LogBoxSD(connection)

    #dateformat: YY-mm-dd
    def sendDataToServer(self, date):
        data = self.getData(date)
        for register in data:
            MyRequest.sendData(register)

    def getData(self, date):

        self.logBoxSD.serviceModeState()
        self.logBoxSD.sdMode()
        fileNumber = self.__getFileNumber(date)
        return self.__parseData(self.logBoxSD.getFileData(fileNumber))

    def __getFileNumber(self, date):
        for fileName in self.logBoxSD.listFiles():
            if date == self.__getDateOfFileName(fileName):
                return self.__getFileNumberOfFileName(fileName)
        return -1

    def __getDateOfFileName(self, str):
        if "SD card size:" in str:
            return -1
        split = str.split(" ")
        return split[3]

    def __getFileNumberOfFileName(self, str):
        return int(str.split(" ")[0][4:-4])

    def __parseData(self, registers):
        parsedRegisters = []
        for register in registers:
            parsedRegisters.append(self.__parseRegister(register))
        return parsedRegisters

    def __parseRegister(self, split):
        data = Data(
                date=split[0],
                time=split[1],
                data1=split[3],
                data2=split[6],
                data3=split[9]
        )

        return data
