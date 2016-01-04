import socket


class MySocket:

    __MSGLEN = 1

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mySendAndReceive(self, msg):
        totalSent = 0
        while totalSent < self.__MSGLEN:
            sent = self.sock.send(msg[totalSent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalSent = totalSent + sent

        self.sock.send(msg + "\n")

        # Look for the response
        amount_received = 0
        amount_expected = len(msg)

        while amount_received < amount_expected:
            data = self.sock.recv(8192)
            amount_received += len(data)

        return data