# -*- coding: utf-8 -*-
from enum import Enum

class Connection:
    """
    Interface to provide communication methods that
    must be implemented by the definition of the specific
    connection mechanism
    """
    def __init__(self):
        pass

    def receive(self):
        raise NotImplementedError("Should have implemented this")

    def send(self, msg):
        raise NotImplementedError("Should have implemented this")

    def close(self):
        raise NotImplementedError("Should have implemented this")

    def __str__(self):
        raise NotImplementedError("Should have implemented this")

from Connection.TCPConnection import TCPConnection
from Connection.TTYConnection import TTYConnection

class ConnectionType(Enum):
    TCP = TCPConnection
    TTY = TTYConnection