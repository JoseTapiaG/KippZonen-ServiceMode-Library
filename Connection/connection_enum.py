from enum import Enum

from Connection.TCPConnection import TCPConnection
from Connection.TTYConnection import TTYConnection


class ConnectionType(Enum):
    TCP = TCPConnection
    TTY = TTYConnection