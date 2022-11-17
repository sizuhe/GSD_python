import serial.tools.list_ports
import random



class SerialComm:
    def __init__(self):
        self.serialInst = serial.Serial()
        self.serialInst.baudrate = 9600
        self.testPort = False
        arduinoSignal = False

        # Automatic arduino detection
        if len(serial.tools.list_ports.comports()) != 0:
            for port in serial.tools.list_ports.comports():
                if ('CH340' or 'Arduino') in port.description:
                    arduinoSignal = True
                    self.serialInst.port = port.name
                    self.serialInst.open()
                elif arduinoSignal == False:
                    self.testPort = True
        else:
            self.testPort = True

        # Manual mode
        # self.serialInst.port = "COM4"       
        # self.serialInst.open()

    # Reading data
    def dataPacket_Read(self):
        # Reading data from from serial port
        #* arduino print speed 500 ms
        if self.testPort == False:
            try:
                packet = self.serialInst.readline()
                packet = packet.decode("utf-8")
                packet = packet.split(',')
                return packet
            except:
                print("Error en la decodificación de datos")
        # Test mode
        else:
            packet = [0, random.random(), random.random(), random.random(), random.random()]
            return packet

    def testStatus(self):
        return self.testPort