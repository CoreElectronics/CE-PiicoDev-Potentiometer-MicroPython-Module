/*
  User accessible functions
*/

// Macro for number of elements in an array
#define COUNT_OF(x) ((sizeof(x)/sizeof(0[x])) / ((size_t)(!(sizeof(x) % sizeof(0[x])))))

void readPotentiometer(char *data) {
  #if DEBUG
    Serial.println(analogRead(potentiometerPin));
  #endif
  valueMap.pot = analogRead(potentiometerPin);
  responseType = RESPONSE_VALUE;
  loadArray((unsigned int)valueMap.pot);
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS); //Command success
}

void idReturn(char *data) {
  responseType = RESPONSE_VALUE;
  loadArray((unsigned int)valueMap.id);
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS); //Command success
}

void statusReturn(char *data) {
  responseType = RESPONSE_VALUE;
  loadArray((byte)valueMap.status);
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS); //Command successful. Set status bit.
}

void firmwareMajorReturn(char *data) {
  responseType = RESPONSE_VALUE;
  loadArray((byte)valueMap.firmwareMajor);
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS); //Command success
}

void firmwareMinorReturn(char *data) {
  responseType = RESPONSE_VALUE;
  loadArray((byte)valueMap.firmwareMinor);
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS); //Command success
}

// Control the power LED brightness
void setPowerLed(char *data) {
//  analogWrite(powerLedPin, data[0]);
//  valueMap.debug = data[0];
    powerLed( (data[0] == 1) );
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS);
}

//void powerLed(bool state) {
//  if (state) {
//    analogWrite(powerLedPin, 254);
//  } else {
//    analogWrite(powerLedPin, 0);
//  }
//}

void powerLed(bool state) {
  if (state) {
    digitalWrite(powerLedPin, true);
  } else {
    digitalWrite(powerLedPin, false);
  }
}

void debugReturn(char *data) {
  responseType = RESPONSE_VALUE;
  loadArray(valueMap.debug);
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS); //Command success
}

void setAddress(char *data) {
  byte tempAddress = data[0];

  if (tempAddress < 0x08 || tempAddress > 0x77)
    return; //Command failed. This address is out of bounds.
  valueMap.i2cAddress = tempAddress;

  EEPROM.put(LOCATION_ADDRESS_TYPE, SOFTWARE_ADDRESS);
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS);
  updateFlag = true; // will trigger a I2C re-initalise and save custom address to EEPROM
}


//Loads a long into the start of the responseBuffer
void loadArray(unsigned long myNumber)
{
  for (byte x = 0 ; x < sizeof(myNumber) ; x++)
    responseBuffer[x] = (myNumber >> (((sizeof(myNumber) - 1) - x) * 8)) & 0xFF;
  responseSize = sizeof(myNumber);
}

void loadArray(long myNumber)
{
  for (byte x = 0 ; x < sizeof(myNumber) ; x++)
    responseBuffer[x] = (myNumber >> (((sizeof(myNumber) - 1) - x) * 8)) & 0xFF;
  responseSize = sizeof(myNumber);
}

//Loads an int into the start of the responseBuffer
void loadArray(int myNumber)
{
  for (byte x = 0 ; x < sizeof(myNumber) ; x++)
    responseBuffer[x] = (myNumber >> (((sizeof(myNumber) - 1) - x) * 8)) & 0xFF;
  responseSize = sizeof(myNumber);
}

void loadArray(unsigned int myNumber)
{
  for (byte x = 0 ; x < sizeof(myNumber) ; x++)
    responseBuffer[x] = (myNumber >> (((sizeof(myNumber) - 1) - x) * 8)) & 0xFF;
  responseSize = sizeof(myNumber);
}

//Loads an byte into the start of the responseBuffer
void loadArray(byte myNumber)
{
  for (byte x = 0 ; x < sizeof(myNumber) ; x++)
    responseBuffer[x] = (myNumber >> (((sizeof(myNumber) - 1) - x) * 8)) & 0xFF;
  responseSize = sizeof(myNumber);
}

//Loads a bool into the start of the responseBuffer
void loadArray(boolean myStatus)
{
  responseBuffer[0] = myStatus;
  responseSize = sizeof(myStatus);
}
