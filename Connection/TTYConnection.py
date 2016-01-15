# -*- coding: utf-8 -*-

from Connection.Connection import Connection
from Exceptions import TTYConnectionError
import serial


class TTYConnection(Connection):
    """
    Implementation of a Connection using serial devices as tty devices
    test with: socat -d -d pty,raw,ignbrk=0,cs8,cstopb=0,b115200 pty,raw,ignbrk=0,cs8,cstopb=0,b115200
    """

    def __init__(self, port='/dev/ttyUSB1'):
        Connection.__init__(self)
        self.conn = serial.Serial()
        self.set_serial_configuration(port)
        try:
            self.conn.open()
            self.conn.flushInput()
            self.conn.flushOutput()
        except serial.SerialException as e:
            raise TTYConnectionError(e)

    # setSerialConfiguration: None -> None
    # SetUp configurations for serial tty connections
    def set_serial_configuration(self, port):
        self.conn.port = port
        self.conn.baudrate = 115200
        self.conn.bytesize = serial.EIGHTBITS
        self.conn.parity = serial.PARITY_NONE
        self.conn.stopbits = serial.STOPBITS_ONE
        self.conn.timeout = 0  # Non-Block reading
        self.conn.xonxoff = False  # Disable Software Flow Control
        self.conn.rtscts = False  # Disable (RTS/CTS) flow Control
        self.conn.dsrdtr = False  # Disable (DSR/DTR) flow Control
        self.conn.writeTimeout = 2

    # receive: None -> String
    # Read the full available data in the tty serial port
    def receive(self):
        data = self.conn.read(1)
        len_data = len(data)
        while len_data > 0:
            aux = self.conn.read(1)
            len_data = len(aux)
            data += aux
        return data

    # send: String -> Int
    # Write a msg String into the serial tty port and return the number of bytes written
    def send(self, msg):
        return self.conn.write(msg)

    # close: None -> None
    # Close the connection
    def close(self):
        return self.conn.close()

    # None -> String
    # Return a String representation of the object
    def __str__(self):
        return "TTYConnection Object: \n" + str(self.conn)
