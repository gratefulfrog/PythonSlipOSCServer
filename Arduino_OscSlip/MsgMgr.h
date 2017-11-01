#ifndef MSGGR_H
#define MSGGR_H

#include <Arduino.h>

#include <OSCMessage.h>
#include <SLIPEncodedSerial.h>

#define BAUDRATE (115200)

#include "stdDefs.h"

class MsgMgr{
  protected:
    SLIPEncodedSerial *SLIPSerial;

  public:
    MsgMgr();
    void send(u8u32f_struct *t);
    void send(int i);

};

#endif
  
