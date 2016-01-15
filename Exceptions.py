# -*- coding: utf-8 -*-

"""
    Exceptions raised in Library
"""


# Exceptions raised in LogBoxSD class
class MethodNotFound(Exception):
    def __init__(self):
        print "Error: Method not found"

# Exceptions raised in TCPConnection class
class TCPConnectionError(Exception):
    def __init__(self):
        print "Error: Connection refused by host"

# Exceptions raised in TTYConnection class
class TTYConnectionError(Exception):
    def __init__(self, msg):
        print "Error: ", msg