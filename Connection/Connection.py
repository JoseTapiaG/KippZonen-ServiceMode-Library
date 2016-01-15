# -*- coding: utf-8 -*-


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
