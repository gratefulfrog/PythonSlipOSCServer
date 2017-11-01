#ifndef STDDEFS_H
#define STDDEFS_H

/** This is the stuct used to handle data read from the sensors as well as all SPI responses to the Master
 */
struct u8u32f_struct{
  uint8_t  u8;  //<! this value encodes the ADC id and the Channel id on a byte, high 4 bits are ADC id, low 4 bits are channel id
  uint32_t u32; //<! this is the timestamp value
  float    f;   //<!this is the sensor value
  
  /* operators used in comparisons for this struct type
   */
  boolean operator==(const u8u32f_struct& r) const {
    return (u8 == r.u8) &&
           (u32 == r.u32) &&
           (f == r.f);
  }
  /* operators used in comparisons for this struct type
   */boolean operator!=(const u8u32f_struct& r) const {
    return !(*this == r);
  }
} __attribute__((__packed__));  //<! packing ensures that onlyt the 9 bytes needed by the struct are used in memory

#endif
