#include "MsgMgr.h"

MsgMgr::MsgMgr(){
  SLIPSerial = new SLIPEncodedSerial(Serial);
  SLIPSerial->begin(BAUDRATE); //begin(115200);
}

void MsgMgr::send(u8u32f_struct *t){
  //the message wants an OSC address as first argument
  OSCMessage msg("/iif");
  msg.add((unsigned)t->u8);
  msg.add(t->u32);
  msg.add(t->f);

  SLIPSerial->beginPacket();  
  msg.send(*SLIPSerial); // send the bytes to the SLIP stream
  SLIPSerial->endPacket(); // mark the end of the OSC Packet
  msg.empty(); // free space occupied by message
}

void MsgMgr::send(int i){
  //the message wants an OSC address as first argument
  OSCMessage msg("/i");
  msg.add(i);

  SLIPSerial->beginPacket();  
  msg.send(*SLIPSerial); // send the bytes to the SLIP stream
  SLIPSerial->endPacket(); // mark the end of the OSC Packet
  msg.empty(); // free space occupied by message
}


