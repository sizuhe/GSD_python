import serial.tools.list_ports
import random



class SerialComm:
    def __init__(self):
        self.serialInst = serial.Serial()
        self.serialInst.baudrate = 9600
        self.testSignal = False
        self.arduinoName = 'Testmode'
        arduinoList = ['Arduino', 'CH340']

        # Automatic arduino detection and test mode
        if len(serial.tools.list_ports.comports()) != 0:
            for port in serial.tools.list_ports.comports():
                for arduino in arduinoList:
                    if port.description.find(arduino) != -1:
                        self.serialInst.port = port.name
                        self.arduinoName = port.description
                        self.serialInst.open()
                        break
                    else:
                        self.testSignal = True
                break
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
            except Exception as error:
                print("Error serialcomm - Serial port data reading")
                print(error)
        # Test mode data
        else:
            packet = [random.random(),
                      random.random(),
                      random.random(),
                      random.random(),
                      random.random(),
                      random.random(),
                      random.random(),
                      random.random()]
            return packet

    def getTestStatus(self):
        return self.testSignal
    
    def getArduinoName(self):
        return self.arduinoName