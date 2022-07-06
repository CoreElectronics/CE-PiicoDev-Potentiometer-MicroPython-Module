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
  loadArray((uint16_t)valueMap.pot);
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS);
}

void idReturn(char *data) {
  responseType = RESPONSE_VALUE;
  loadArray((uint16_t)valueMap.id);
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS);
}

void firmwareMajorReturn(char *data) {
  responseType = RESPONSE_VALUE;
  loadArray((uint8_t)valueMap.firmwareMajor);
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS);
}

void firmwareMinorReturn(char *data) {
  responseType = RESPONSE_VALUE;
  loadArray((uint8_t)valueMap.firmwareMinor);
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS);
}

// Control the power LED
void getPowerLed(char *data) {
  responseType = RESPONSE_VALUE;
  valueMap.led = digitalRead(powerLedPin);
  loadArray((uint8_t)valueMap.led);
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS);
}

// Control the power LED
void setPowerLed(char *data) {
  powerLed( (data[0] == 1) );
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS);
}

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
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS);
}

void setAddress(char *data) {
  uint8_t tempAddress = data[0];

  if (tempAddress < 0x08 || tempAddress > 0x77)
    return; // Command failed. This address is out of bounds.
  valueMap.i2cAddress = tempAddress;

  EEPROM.put(LOCATION_ADDRESS_TYPE, SOFTWARE_ADDRESS);
  valueMap.status |= (1 << STATUS_LAST_COMMAND_SUCCESS);
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
