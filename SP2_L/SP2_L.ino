//slave
#include <TinyGPS++.h>
#include <SoftwareSerial.h>
#include <Wire.h>
#include <SPI.h>
#define destination 0x08
#define LED 3
static const int RXPin = 8, TXPin = 9;
static const uint32_t GPSBaud = 9600;

TinyGPSPlus gps;
SoftwareSerial ss(RXPin, TXPin);

char missionTime[32] = "XX:XX:XX";

float G_latitude = 0;
float G_longitude = 0;

String GPS = "";
String packet = "";

void setup() {
  Serial.begin(9600);
  ss.begin(GPSBaud);
  
  Serial.println("[SETUP]");
  
  pinMode(LED,OUTPUT);
  Wire.begin(destination);
  Wire.onRequest(requestEvent);
  Wire.onReceive(receiveEvent);
}
void get_gps(){
  while (ss.available()) gps.encode(ss.read());
  if (gps.location.isValid())
  {
    G_latitude = gps.location.lat();
    G_longitude = gps.location.lng();
    GPS = String(G_latitude,6) + "," + String(G_longitude,6);
  }
  if (gps.time.isValid())
  {
    sprintf(missionTime, "%02d:%02d:%02d", gps.time.hour(), gps.time.minute(), gps.time.second());
  }
}

void loop() {
  get_gps();
}

void receiveEvent(){
  digitalWrite(LED,HIGH);
  String inp="";
  while(Wire.available()){
    char c = Wire.read();
    inp+=c;
  }
  if (inp=="gt"){packet=missionTime;}
  else if (inp=="ga")
  {
    packet=String(G_latitude,6);
    for(int i=packet.length();i<=10;i++)
    {
      packet += "S";
    }
  }
  else if (inp=="go")
  {
    packet=String(G_longitude,6);
    for(int i=packet.length();i<=10;i++)
    {
      packet += "S";
    }
  }
}
void requestEvent(){
  digitalWrite(LED,LOW);
  char a[20];
  packet.toCharArray(a,20);
  Wire.write(a);
}
