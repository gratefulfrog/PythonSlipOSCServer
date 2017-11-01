#!/usr/bin/python3

import serial
from time import sleep
from OSC import decodeOSC
from slipDecoder import SlipDecoder

class OSCProcessor():
    def __init__(self):
        self.fDict = {'/i'  :self.doSingleton,
                      '/iif':self.doStruct}

    def doSingleton(self,singletonLis):
        print(singletonLis[0])
        
    def doStruct(self,structLis):
        adcChid = structLis[0]
        timeStamp = structLis[1]
        value = round(structLis[2],3)
        print(adcChid,timeStamp,value)
    
    def dispatchOSCList(self,oscLis):
        self.fDict[oscLis[0]](oscLis[2:])


class SerialServer():
    def __init__(self, portT, bd = 115200, to = None):
        self.port        = portT
        self.stopEvent   = False
        self.baudrate    = bd
        self.timeout     = to
        self.slipDecoder = SlipDecoder()
        self.dispatcher  = OSCProcessor()
        
    def serve(self):
        with serial.Serial(port = self.port, baudrate= self.baudrate, timeout = self.timeout) as ser:
            sleep(1)
            # first clear anything on the incoming port
            ser.timeout = 0
            while ser.read():
                pass
            ser.timeout = self.timeout

            # now give the handshake!
            sleep(1)
            ser.write(b'|')
            sleep(1)
            print('Started... ctrl-C to exit')
            
            while True:
                try:
                    if self.stopEvent:
                        print('\nexting...')
                        break
                    res = self.slipDecoder.decodeFromSLIP(ser.read(16)) # 16 bytes
                    if res:
                        # we got a complete OSC message and can dispatch it
                        self.dispatcher.dispatchOSCList(decodeOSC(bytes(res)))
                    # now continue serving...
                except KeyboardInterrupt:
                    self.stopEvent = True
            
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        server = SerialSever(sys.argv[1])
    else:
        server = SerialServer('/dev/ttyACM0')
    server.serve()
