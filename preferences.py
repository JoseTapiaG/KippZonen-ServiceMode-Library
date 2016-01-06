import serial #module pyserial - sudo pip install pyserial

connectionClass="tty"
moduleName="tty"
port='/dev/ttyUSB1',
baudrate=115200,
parity=serial.PARITY_ODD,
stopbits=serial.STOPBITS_TWO,
bytesize=serial.EIGHTBITS