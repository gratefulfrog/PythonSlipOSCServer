
class ProtocolError(Exception):
    pass

class SlipDecoder():
    SLIP_END     = 0o300   # 192 0xC0
    SLIP_ESC     = 0o333   # 219 0xDB
    SLIP_ESC_END = 0o334   # 220 0xDC
    SLIP_ESC_ESC = 0o335   # 221 0xDD
    
    def __init__(self):
        self.dataBuffer = []
        self.carry      = bytes([])
        self.carryBytes = bytes([])
        self.reset      = False
        
    def resetForNewBuffer(self):
        self.dataBuffer = []
        self.carry = bytes([])
        self.reset = False

    def decodeFromSLIP(self,bytesIn): 
        """
        arguments are bytes to decode
        return decode values as list or None if not available,
        carry over values are accumulated so partial messages work ok
        """
        if self.reset:
            self.resetForNewBuffer()

        serialFD=iter(self.carry + self.carryBytes + bytesIn)
        try:        
            while True:
                serialByte = next(serialFD)           ## could raise StopIteration, so carry better be right!
                if serialByte == SlipDecoder.SLIP_END:
                    if len(self.dataBuffer) > 0:       ## true if this is not a 'start byte'
                        self.carryBytes=bytes(serialFD)
                        self.reset = True
                        return self.dataBuffer         ## exit the while loop HERE only!
                elif serialByte == SlipDecoder.SLIP_ESC:
                    self.carry = bytes([SlipDecoder.SLIP_ESC])
                    serialByte = next(serialFD)        ## could raise  StopIteration, with new carry
                    if serialByte == SlipDecoder.SLIP_ESC_END:
                        self.dataBuffer.append(SlipDecoder.SLIP_END)
                    elif serialByte == SlipDecoder.SLIP_ESC_ESC:
                        self.dataBuffer.append(SlipDecoder.SLIP_ESC)
                    else:
                        raise ProtocolError
                else:
                    self.carry=bytes([])    ## in case of  StopIteration exception at top of loop
                    self.dataBuffer.append(serialByte)
        except StopIteration:
            self.carryBytes = bytes(serialFD)
            return None  # here reset is false
