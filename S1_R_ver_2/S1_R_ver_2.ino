#include <SD.h>
#include <SPI.h>
#include <SoftwareSerial.h>
#include <EEPROM.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#define LED 3
#define destination 0x08
#define SEALEVELPRESSURE_HPA (1013.25)

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

char FileS1[100];
unsigned int packetcount = 0;
String Altitude = "aaaa";
String Temp = "aaaa";
String Accx = "aaaa";
String Accy = "aaaa";
String Accz = "aaaa";
int recoveryalt;
//String telemetry = "aaaaaaaaaaaaaaaaaaa";
//String telemetry2 = "aaaaaaaaaaaaaaaaaa";
//String telemetry3 = "aaaaaaaaaaaaaaaaaa";

void setup() {
  Serial.begin(9600);
  xbee.begin(9600);
  Wire.begin();
  Serial.println("[SETUP]");
  bme.begin(0x76, &Wire);
  pinMode(LED,OUTPUT);
  digitalWrite(LED,HIGH);
  delay(100);
  digitalWrite(LED,LOW);
  delay(100);
  
  if (!bno.begin()){
    for( int i =0;i<2;i++){
      digitalWrite(LED,HIGH);
      delay(100);
      digitalWrite(LED,LOW);
      delay(100);
    }
    Serial.println("[BNO]");
  }
  if(!SD.begin(chipSelect)){
    for( int i =0;i<3;i++){
      digitalWrite(LED,HIGH);
      delay(100);
      digitalWrite(LED,LOW);
      delay(100);
    }
    Serial.println("[SD]");
  }
  recovery();
}
void recovery(){
  int recoveryon = EEPROM.read(refon);
  recoveryalt = EEPROM.read(refalt);
  Serial.println(recoveryon);
  Serial.println(recoveryalt);
  if (recoveryalt == 0){
    recoveryalt = round(bme.readAltitude(SEALEVELPRESSURE_HPA));
    EEPROM.put(refalt, recoveryalt);
  }
  if (recoveryon == 0) {
    Serial.print("OFF");
    packetcount = 0;
    startprogram = false;
  }
  else {
    Serial.print("ON");
    startprogram = true;
    packetcount = EEPROM.read(refpkg);
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
void get_bme(){
  Temp = bme.readTemperature();
  Altitude = (bme.readAltitude(SEALEVELPRESSURE_HPA)) - recoveryalt;
}
void get_acc(){
  imu::Vector<3> acc = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  Accx = String(acc.x());
  Accy = String(acc.y());
  Accz = String(acc.z());
}

void loop() {
  while (xbee.available()){
    String income = xbee.readStringUntil('$');
    income.trim();
    if (income == "CMD,3751,SP1X,ON"){
      startprogram = true;
      packetcount = 0;
      EEPROM.write(refon, 1);
      EEPROM.write(refpkg, 0);
    }
    else if (income == "CMD,3751,SP1X,OFF"){
      startprogram =false;
      for (int i = 0 ; i < EEPROM.length() ; i++) {
          EEPROM.write(i, 0);
      }
    }
  }
  if (startprogram){
    time1=millis();
    if (time1-time0 >= 1000){
      get_bme();
      imu::Vector<3> gyro = bno.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);
      String Rotation = String(abs(gyro.x() * 9.549297));
      get_acc();
      packetcount +=1;
      String MISSIONTIME = "";
      Wire.beginTransmission(destination);
      Wire.write("gt"); 
      Wire.endTransmission();
      Wire.requestFrom(destination,8);
      while (Wire.available()){
        char c = Wire.read();
        MISSIONTIME += c;
      }
      delay(50);
      String lati = "";
      Wire.beginTransmission(destination);
      Wire.write("ga");
      Wire.endTransmission();
      Wire.requestFrom(destination, 10);
        while (Wire.available()){
          char c = Wire.read();
          if(c != 'S') lati+=String(c);
      }
      delay(50);
      String longi = "";
      Wire.beginTransmission(destination);
      Wire.write("go");
      Wire.endTransmission();
      Wire.requestFrom(destination,10);
      while (Wire.available()){
        char c = Wire.read();
        if(c != 'S') longi += String(c);
     }   
                             
      if(packetcount%2==0){
        digitalWrite(LED,HIGH);
      }else{
        digitalWrite(LED,LOW);
      }
      xbee.print("3751,");
      xbee.print(MISSIONTIME);
      xbee.print(",");
      xbee.print(packetcount);
      xbee.print(",SP1,");
      xbee.print(Altitude);
      xbee.print(",");
      xbee.print(Temp);
      xbee.print(",");
      xbee.print(Rotation);
      xbee.print(",");
      xbee.print(lati);
      xbee.print(",");
      xbee.print(longi);
      xbee.print(",");
      xbee.print(Accx);
      xbee.print(",");
      xbee.print(Accy);
      xbee.print(",");
      xbee.print(Accz);
      xbee.println("$");
      EEPROM.put(refpkg,packetcount);
      File file = SD.open(FileS1, FILE_WRITE);
      if (file){
        file.print("3571,");
        file.print(MISSIONTIME);
        file.print(",");
        file.print(packetcount);
        file.print(",SP1,");
        file.print(Altitude);
        file.print(",");
        file.print(Temp);
        file.print(",");
        file.print(Rotation);
        file.print(",");
        file.print(lati);
        file.print(",");
        file.print(longi);
        file.print(",");
        file.print(Accx);
        file.print(",");
        file.print(Accy);
        file.print(",");
        file.print(Accz);
        file.println("$");
        file.close();
      }
      time0 = time1;
      }
  }
  else{
    digitalWrite(LED,LOW);
  }
}
