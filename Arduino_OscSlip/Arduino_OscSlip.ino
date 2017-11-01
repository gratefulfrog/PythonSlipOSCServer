#include <Arduino.h>

#include "stdDefs.h"
#include "MsgMgr.h"

//#define SEND_INTS  // uncomment to send ints only

MsgMgr *comms;

#ifndef SEND_INTS
u8u32f_struct s = {0,0,0.0};
#endif

void handShake(){
  while (Serial.available() <=0){
  }
}

void setup() {
  Serial.begin(BAUDRATE);
  while(!Serial);
  handShake();
  
  comms = new MsgMgr();
}

void loop() {
#ifdef SEND_INTS
  static int i=0;
  comms->send(i++);
#else
  comms->send(&s);
  s.u8++;
  s.u32+=10;
  s.f+=0.001;
  if(s.u8==0){
    s.u32 = 0;
    s.f   = 0.0;  
  }
#endif
  delay(500);
}
