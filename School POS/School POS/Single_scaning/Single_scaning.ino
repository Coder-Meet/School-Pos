#include "SPI.h" // SPI library
#include "MFRC522.h" // RFID library (https://github.com/miguelbalboa/rfid)

const int pinRST = 9;
const int pinSDA = 10;

MFRC522 mfrc522(pinSDA, pinRST); // Set up mfrc522 on the Arduino
String previous_tag="";

void setup() {
  
  SPI.begin(); // open SPI connection
  mfrc522.PCD_Init(); // Initialize Proximity Coupling Device (PCD)
  Serial.begin(9600); // open serial connection
}

void loop() {
  String tag="";
  if (mfrc522.PICC_IsNewCardPresent()) { // (true, if RFID tag/card is present ) PICC = Proximity Integrated Circuit Card
    if(mfrc522.PICC_ReadCardSerial()) { // true, if RFID tag/card was read
      for (byte i = 0; i < mfrc522.uid.size; ++i) { // read id (in parts)
        tag+=mfrc522.uid.uidByte[i];
        tag+=" ";
      }
      if (tag != previous_tag){
        Serial.println(tag); 
      previous_tag = tag;
      tag = "";
      }
      }
  }
  }
