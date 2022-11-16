import serial.tools.list_ports
import random



class SerialComm:
    def __init__(self):
        self.serialInst = serial.Serial()
        self.serialInst.baudrate = 9600
        self.testPort = False
        arduinoSignal = False

        # Automatic arduino detection
        for port in serial.tools.list_ports.comports():
            if ('CH340' or 'Arduino') in port.description:
                arduinoSignal = True
                self.serialInst.port = port.name
                self.serialInst.open()
            elif arduinoSignal == False:
                self.testPort = True

        # Manual mode
        # self.serialInst.port = "COM4"       
        # self.serialInst.open()

    # Reading data
    def dataPacket_Read(self):
        # Test mode
        if self.testPort == True:
            packet = [0, random.random(), random.random(), random.random()]
            return packet

        # Reading data from from serial port
        #* arduino print speed 500 ms
        else:
            try:
                # serialInst = serial.Serial(portName, baudrate)
                packet = self.serialInst.readline()
                packet = packet.decode("utf")
                packet = packet.split(',')
                return packet
            except:
                print("Error en la decodificación de datos")

    def testStatus(self):
        return self.testPort