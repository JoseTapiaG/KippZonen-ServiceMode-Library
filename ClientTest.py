from Client import Client
from MySocket import MySocket

# mySocket = MySocket()

# mySocket.connect("localhost", 9090)

# print mySocket.mySendAndReceive("\x03\n")
# print mySocket.mySendAndReceive("s\n")
# print mySocket.mySendAndReceive("l\n")
# print mySocket.mySendAndReceive("t\n")
# print mySocket.mySendAndReceive("1\n")
# print mySocket.mySendAndReceive("2\n")
# print mySocket.mySendAndReceive("3\n")
#
# print mySocket.mySendAndReceive("c\n")
client = Client("localhost", 9090)

for data in client.getDayData("2007-06-20"):
    print  data.date + " " + data.time + " " + data.data1 + " " + data.data2 + " " + data.data3 + "\n"
