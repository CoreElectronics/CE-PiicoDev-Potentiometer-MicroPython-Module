/*
  User accessible functions
*/

void readPotentiometer(char *data) {
  #if DEBUG
    Serial.println(analogRead(potentiometerPin));
  #endif
  valueMap.pot = analogRead(potentiometerPin);
  loadArray((uint16_t)valueMap.pot);
}

void idReturn(char *data) {
  loadArray((uint16_t)valueMap.id);
}

void firmwareMajorReturn(char *data) {
  loadArray((uint8_t)valueMap.firmwareMajor);
}

void firmwareMinorReturn(char *data) {
  loadArray((uint8_t)valueMap.firmwareMinor);
}

void getPowerLed(char *data) {
  valueMap.led = digitalRead(powerLedPin);
  loadArray((uint8_t)valueMap.led);
}

void setPowerLed(char *data) {
  powerLed( (data[0] == 1) );
}

void powerLed(bool state) {
  digitalWrite(powerLedPin, state);
}

void setAddress(char *data) {
  uint8_t tempAddress = data[0];

  if (tempAddress < 0x08 || tempAddress > 0x77)
    return; // Command failed. This address is out of bounds.
  valueMap.i2cAddress = tempAddress;

  EEPROM.put(LOCATION_ADDRESS_TYPE, SOFTWARE_ADDRESS);
  updateFlag = true; // will trigger a I2C re-initalise and save custom address to EEPROM
}

// Functions to load data into the response buffer
void loadArray(uint8_t myNumber)
{
  for (uint8_t x = 0 ; x < sizeof(myNumber) ; x++)
    responseBuffer[x] = (myNumber >> (((sizeof(myNumber) - 1) - x) * 8)) & 0xFF;
  responseSize = sizeof(myNumber);
}

void loadArray(uint16_t myNumber)
{
  for (uint8_t x = 0 ; x < sizeof(myNumber) ; x++)
    responseBuffer[x] = (myNumber >> (((sizeof(myNumber) - 1) - x) * 8)) & 0xFF;
  responseSize = sizeof(myNumber);
}
