//PL right processor
//master
#include <SD.h>
#include <SPI.h>
#include <Wire.h>
#include <SoftwareSerial.h>
#include <EEPROM.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#define LED 3
#define destination 0x08
#define SEALEVELPRESSURE_HPA (1013.25)
//other variable
Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);
Adafruit_BME280 bme;

SoftwareSerial xbee(8, 9);

const int chipSelect = 10;
unsigned long time0 = 0;
unsigned long time1 = 0;

const int refon = 1;
const int refpkg = 10;
const int refalt = 20;

bool startprogram = true;

// main data;
char FileS1[100];
String MISSIONTIME = "";
unsigned int packetcount = 0;
String Rotation = "";
String Altitude = "";
String Temp = "";
String GPS = "";
String telemetry = "";
String telemetry2 = "";
String lati = "";
String longi = "";
int recoveryalt;

void setup() {
  Serial.begin(9600);
  xbee.begin(9600);
  bme.begin(0x76, &Wire);
  if (!bno.begin()){
    Serial.println("bno error");
  }
  pinMode(LED,OUTPUT);
  Wire.begin(); 
  if(!SD.begin(chipSelect)){
    for(int i=0;i<5;i++){
      digitalWrite(LED,HIGH);
      delay(100);
      digitalWrite(LED,LOW);
      delay(100);
    }
  }
  bno.setExtCrystalUse(true);
  recoveryalt = round(bme.readAltitude(SEALEVELPRESSURE_HPA));
  EEPROM.put(refalt, recoveryalt);
  recovery();
}
void get_bme(){
  Temp = bme.readTemperature();
  Altitude = (bme.readAltitude(SEALEVELPRESSURE_HPA)) - recoveryalt;
}
void get_bno(){
  imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);
  Rotation = String(abs(euler.x() * 9.549297));
}
void recovery(){
  int recoveryon = EEPROM.read(refon);
  if (recoveryon == 1){
    Serial.print("ON");
    startprogram = true;
    packetcount = EEPROM.read(refpkg);
    recoveryalt = EEPROM.read(refalt);
    }
  else {
    Serial.print("OFF");
    startprogram = false;
    packetcount = 0;
    }
  int idx = 0;
  String S1 = ("S1I" + String(idx)+".txt");
  S1.toCharArray(FileS1, 100);
  while (SD.exists(FileS1))
  {
    idx++;
    S1 = ("S1I" + String(idx) + ".txt");
    S1.toCharArray(FileS1, 100);
  }
}
void loop(){
  if (xbee.available()){
     String income = xbee.readStringUntil('$');
      income.trim();
      if (income == "CMD,3751,SP1X,ON"){
        startprogram = true;
        EEPROM.write(refon, 1);
        packetcount = 0;
      }
      else if (income == "CMD,3751,SP1X,OFF"){
        startprogram = false;
        EEPROM.write(refon, 0);
        for (int i = 0 ; i < EEPROM.length() ; i++) {
          EEPROM.write(i, 0);
        }
      }
    }
  if (startprogram){
    time1 = millis();
    if (time1 - time0 >= 1000){
      get_bno();
      get_bme();
      packetcount += 1;
                    MISSIONTIME = "";
                    Wire.beginTransmission(destination);
                    Wire.write("gt"); 
                    Wire.endTransmission();
                    Wire.requestFrom(destination,8);
                    while (Wire.available()){
                      char c = Wire.read();
                      MISSIONTIME += c;
                    }
                    MISSIONTIME.trim();
                    lati = "";
                    Wire.beginTransmission(destination);
                    Wire.write("ga");
                    Wire.endTransmission();
                    Wire.requestFrom(destination, 10);
                      while (Wire.available()){
                        char c = Wire.read();
                        if(c != 'S') lati+=String(c);
                      }
                    longi = "";
                    Wire.beginTransmission(destination);
                    Wire.write("go");
                    Wire.endTransmission();
                    Wire.requestFrom(destination,10);
                    while (Wire.available()){
                      char c = Wire.read();
                      if(c != 'S') longi += String(c);
                    }
      digitalWrite(LED,HIGH);
      telemetry = "3751," + MISSIONTIME + "," + String(packetcount) + ",S1," + String(Altitude) + ",";
      telemetry2 = String(Temp) + "," + String(Rotation) + "," + lati + "," + longi;
      xbee.print(telemetry);
      Serial.print("T1:"+telemetry);
      delay(50);
      xbee.println(telemetry2);
      Serial.println(telemetry2);
      EEPROM.put(refpkg,packetcount);
      File file = SD.open(FileS1, FILE_WRITE);
      if (file){
        file.print(telemetry);
        file.println(telemetry2);
        file.close();
      }
      time0 = time1;
      }
    }
  else{
    digitalWrite(LED,LOW);
  }
}
