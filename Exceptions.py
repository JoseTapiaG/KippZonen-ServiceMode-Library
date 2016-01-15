# -*- coding: utf-8 -*-

"""
    Exceptions raised in TCPConnection class
"""


class TCPConnectionError(Exception):
    def __init__(self):
        print "Connection refused by host"

"""
    Exceptions raised in LogBoxSD class
"""


class MethodNotFound(Exception):
    def __init__(self):
        print "Method not found"
