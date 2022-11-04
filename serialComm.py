import serial
import serial.tools.list_ports


class SerialComm:
    # Reading data from serial port
    def dataPacket_Read():
        # serialInst = serial.Serial(portName, baudrate)
        serialInst = serial.Serial()
        serialInst.baudrate = 9600
        serialInst.port = "COM4"
        serialInst.open()

        packet = serialInst.readline()
        packet = packet.decode("utf")
        packet = packet.split(',')

        return packet

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