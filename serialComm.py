import serial.tools.list_ports



class SerialComm:
    def __init__(self):
        self.serialInst = serial.Serial()
        self.serialInst.baudrate = 9600
        self.serialInst.port = "COM4"       #? Port might need to be changed
        self.serialInst.open()

    # Reading data from serial port
    # arduino print speed 500 ms
    def dataPacket_Read(self):
        # serialInst = serial.Serial(portName, baudrate)
        packet = self.serialInst.readline()
        packet = packet.decode("utf")
        packet = packet.split(',')

        return packet

    #! ----- TO DO -----
    # Printing available ports
    def Ports():
        portslist = []

        for port in serial.tools.list_ports.comports():
            portslist.append(port.name)

            # print(dir(port))
            # portslist.sort()
            # return port.name
            # print(port.description)

        return portslist