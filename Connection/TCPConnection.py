# -*- coding: utf-8 -*-

from Connection import Connection
from Exceptions import TCPConnectionError
import socket


class TCPConnection(Connection):
    """
    Implementation of a Connection using a Internet TCP Connection as device
    """

    def __init__(self, address='', port=8080):
        Connection.__init__(self)
        # Use a default Socket: Internet socket with TCP
        self.conn = socket.socket()
        try:
            self.conn.connect((address, port))
        except:
            raise TCPConnectionError()

    # receive: None -> String
    # Read the full available data in the Internet Connection
    def receive(self):
        data = self.conn.recv(1)
        len_data = len(data)
        while len_data > 0:
            aux = self.conn.recv(1)
            len_data = len(aux)
            data += aux
        return data

    # send: String -> Int
    # Write a msg String into the Internet Conection and return the number of bytes written
    def send(self, msg):
        return self.conn.send(msg)

    # close: None -> None
    # Close the connection
    def close(self):
        self.conn.close()

    # None -> String
    # Return a String representation of the object
    def __str__(self):
        return "TCPConnection Object: \n" + str(self.conn)