from Data import Data
from LogBoxSD import LogBoxSD


class Monitor:
    # Class provides methods to query for data in the SDCard of LogBoxSD
    def __init__(self, connection):
        self.logBoxSD = LogBoxSD(connection)

    # get_data: Datetime -> Array
    # Return all registers for the date
    def get_data(self, date):
        self.logBoxSD.service_mode_state()
        self.logBoxSD.sd_mode()
        file_number = self.__get_file_number(date)
        return self.__parse_data(self.logBoxSD.get_file_data(file_number))

    def __get_file_number(self, date):
        for file_name in self.logBoxSD.list_files():
            if date == self.__get_date_of_file_name(file_name):
                return self.__get_file_number_of_file_name(file_name)
        return -1

    def __parse_data(self, registers):
        parsed_registers = []
        for register in registers:
            parsed_registers.append(self.__parse_register(register))
        return parsed_registers

    @staticmethod
    def __get_date_of_file_name(file_name):
        if "SD card size:" in file_name:
            return -1
        split = file_name.split(" ")
        return split[3]

    @staticmethod
    def __get_file_number_of_file_name(file_name):
        return int(file_name.split(" ")[0][4:-4])

    @staticmethod
    def __parse_register(split):
        data = Data(
                date=split[0],
                time=split[1],
                data1=split[3],
                data2=split[6],
                data3=split[9]
        )

        return data
