import serial.tools.list_ports
import random



class SerialComm:
    def __init__(self):
        self.serialInst = serial.Serial()
        self.serialInst.baudrate = 9600
        self.testSignal = False
        arduinoSignal = False

        # Automatic arduino detection and test mode
        if len(serial.tools.list_ports.comports()) != 0:
            for port in serial.tools.list_ports.comports():
                if ('CH340' or 'Arduino') in port.description:
                    arduinoSignal = True
                    self.serialInst.port = port.name
                    self.serialInst.open()
                elif arduinoSignal == False:
                    self.testSignal = True
        else:
            self.testSignal = True

        # Manual mode
        # self.serialInst.port = "COM4"       
        # self.serialInst.open()

    def dataPacket_Read(self):
        # Reading data from from serial port
        if self.testSignal == False:
            try:
                packet = self.serialInst.readline()
                packet = packet.decode("utf-8")
                packet = packet.split(',')
                return packet
            except:
                print("Error serialComm - dataPacket_Read")
        # Test mode data
        else:
            packet = [random.random(), random.random(), random.random(), random.random()]
            return packet

    def testStatus(self):
        return self.testSignal