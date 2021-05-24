#include <SD.h>
#include <SPI.h>
#include <EEPROM.h>
#include <Seeed_BME280.h>
#include <TinyGPS++.h>
#include <TimeLib.h>

#define voldivpin A8
#define Solinoid1 9
#define Solinoid2 6
#define LED1 3
#define LED2 4
#define buzzer 2

TinyGPSPlus gps;
BME280 bme280;
time_t RTCTime;

unsigned long time1 = 0;
unsigned long time0 = 0;

bool cxON = false;
bool simEN = false;
bool simAC = false;
bool SIM = false;
int first = 0;

char FileC[100];
char FileS1[100];
char FileS2[100];

float Peak = -2147483648;
int refAltitude = 0;
int state = 0;
int simPressure = 0;

const int recovPkg = 0;
const int recovState = 10;
const int recovMode = 20;
const int recovAlt = 30;

String Telemetry = "";
String S2 = "";
String S1 = "";
String cm = "";

String teamId = "3751";
char missionTime[32] = "xx:xx:xx";
int Packet = 0;
char Mode = 'F';
char S1r = 'N';
char S2r = 'N';
float Altitude = 0;
float Temp = 0;
float Voltage = 0;
char gpsTime[32] = "xx:xx:xx";
float Latitude = 0;
float Longitude = 0;
float gpsAltitude = 0;
int gpsSatellite = 0;
String State = "PRELAUNCH";
int S1p = 0;
int S2p = 0;
String cmdEcho = "----";


void setup() {
  Serial.begin(9600);
  Serial2.begin(9600);
  Serial3.begin(9600);
  Serial4.begin(9600);
  Serial5.begin(9600);
  
  pinMode(Solinoid1, OUTPUT);
  pinMode(Solinoid2, OUTPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(buzzer,OUTPUT);
  pinMode(voldivpin,INPUT);
  
  setSyncProvider(getTeensy3Time);
  bme280.init();
  
  digitalWrite(buzzer,HIGH);
  digitalWrite(Solinoid1,HIGH);
  digitalWrite(Solinoid2,HIGH);
  digitalWrite(LED1,HIGH);
  digitalWrite(LED2,HIGH);
  delay(3000);
  digitalWrite(buzzer,LOW);
  digitalWrite(Solinoid1,LOW);
  digitalWrite(Solinoid2,LOW);
  digitalWrite(LED1,LOW);
  digitalWrite(LED2,LOW);
  
  if (!SD.begin(10)) {
    for (int i=0;i<5;i++){
    digitalWrite(buzzer,HIGH);
    delay(50);
    digitalWrite(buzzer,LOW);
    delay(50);
    }}
  Serial.println("[DONE SETUP]");
  recovery();
}
void recovery(){
  String a = EEPROM.read(recovPkg);
  String b = EEPROM.read(recovState);
  String c = EEPROM.read(recovMode);
  String d = EEPROM.read(recovAlt);
  int e = c.toInt();
  
  switch (e){
    case 0:  for (int i = 0 ; i < EEPROM.length() ; i++) {
                 EEPROM.write(i, 0);
              }
              cxON = false;
              break;
    case 1:  cxON = true;
              cmdEcho = "CXON";
              Mode = 'F';
              break;
    case 2: cmdEcho = "CXON";
             simEN = true;
             simAC = true;
             Mode = 'S';
             break;
  }
  if (d != '0'){
    refAltitude = d.toInt();
  }else{
    refAltitude = round(float(bme280.calcAltitude(bme280.getPressure())));}
  Packet = a.toInt();
  state = b.toInt();
  get_file();
}
void Command(String cm){
  if (cm == "CX,ON"){
    Serial.println("CXON");
    cxON = true;
    refAltitude = round(float(bme280.calcAltitude(bme280.getPressure())));
    Packet = 0;
    cmdEcho = "CXON";
    state = 0;
    Mode = 'F';
    EEPROM.write(recovMode, 1);
    EEPROM.write(recovAlt, refAltitude);
    EEPROM.write(recovState, state);
    EEPROM.write(recovPkg,0);
    get_file();
  }
  else if (cm == "CX,OFF"){
    Serial.println("CXOFF");
    cxON = false;
    cmdEcho="CXOFF";
    Mode = 'F';
    for (int i = 0 ; i < EEPROM.length() ; i++) {
      EEPROM.write(i, 0);
    }
    digitalWrite(Solinoid1,LOW);
    digitalWrite(Solinoid2,LOW);
    Serial.println("SP1OFF");
    Serial.println("SP2OFF");
    Serial5.print("CMD,3751,SP1X,OFF$");
    Serial4.print("CMD,3751,SP2X,OFF$");
  }
  else if (cm == "SP1X,ON"){
    Serial5.print("CMD,3751,SP1X,ON$");
    S1r='R';
    cmdEcho = "S1ON";
  }
  else if (cm == "SP1X,OFF"){
    Serial5.print("CMD,3751,SP1X,OFF$");
    S1r='N';
    cmdEcho = "S1OFF";
  }
  else if (cm == "SP2X,ON"){
    Serial4.print("CMD,3751,SP2X,ON$");
    S2r='R';
    cmdEcho = "S2ON";
  }
  else if (cm == "SP2X,OFF"){
    Serial4.print("CMD,3751,SP2X,OFF$");
    S2r ='N';
    cmdEcho = "S2OFF";
  }
  else if (cm == "SIM,ENABLE"){
    simEN = true;
    cmdEcho = "SIMEN";
    Serial.println("SIM_EN");
  }
  else if (cm == "SIM,ACTIVATE" && simEN){
    simAC = true;
    cmdEcho = "SIMAC";
    Mode = 'S';
    Serial.println("SIM_AC");
    EEPROM.write(recovMode, 2);
  }
  else if (cm == "SIM,DISABLE"){
    simEN = false;
    simAC = false;
    SIM = false;
    Mode = 'F';
    EEPROM.write(recovMode, 1);
    Serial.println("SIMDIS");
    Command("CX,ON");
  }
  else if (cm.indexOf("SIMP")!=-1 && (simAC&&simEN)){
    cmdEcho = "SIMP";
    simPressure = (cm.substring(5)).toInt();
    Mode = 'S';
    if (first==0){
      SIM = true;
      refAltitude = round(float(bme280.calcAltitude(simPressure)));
      EEPROM.write(recovAlt, refAltitude);
      first = 1;
    }
  }
  else{
    Serial.println(cm);
  }
}
void get_file(){
  int idx = 0;
  String C = ("CI" + String(idx) + ".txt");
  C.toCharArray(FileC,100);
  while (SD.exists(FileC))
  {
    idx++;
    C=("CI" + String(idx) + ".txt");
    C.toCharArray(FileC,100);
  }
  C=("S1I" + String(idx) + ".txt");
  C.toCharArray(FileS1,100);
  C=("S2I" + String(idx) + ".txt");
  C.toCharArray(FileS2,100);
  Serial.println(FileC);
  Serial.println(FileS1);
  Serial.println(FileS2);
}

time_t getTeensy3Time() {
  return Teensy3Clock.get();
}

void get_gps(){
  gps.encode(Serial2.read());
  if (gps.location.isValid()){
    Latitude=gps.location.lat();
    Longitude=gps.location.lng();
    }
  sprintf(gpsTime, "%02d:%02d:%02d", gps.time.hour(), gps.time.minute(), gps.time.second());
  gpsAltitude = gps.altitude.meters();
  gpsSatellite = gps.satellites.value();
}

void get_BME_flight(){
  Temp = bme280.getTemperature();
  float a = bme280.calcAltitude(bme280.getPressure());
  Altitude = float(a-refAltitude);
  if (Altitude>=Peak){
    Peak=Altitude;
  }
}

void get_BME_simulation(){
  Temp = bme280.getTemperature();
  float a = bme280.calcAltitude(simPressure);
  Altitude = float(a-refAltitude);
  if (Altitude>=Peak){
    Peak = Altitude;
  }
}

void get_time(){
  sprintf(missionTime, "%02d:%02d:%02d", hour(), minute(), second());
}

void get_battery(){
  Voltage = (((analogRead(voldivpin) * 0.00080566406)*(4000))/1000)+0.16;
}

void inMission(){
  time1 = millis();
  if (time1-time0>=990){
    get_time();
    get_gps();
    get_battery();
    if (SIM){
      get_BME_simulation();
    }else{
      get_BME_flight();
    }
    switch(state){
      case 0:
        State = "PRELAUNCH";
        if (Altitude >= 10){
          state = 1;
        }break;
      case 1:
        State = "LAUNCH";
        if (Peak-Altitude >= 30 && Altitude > 600){
          state = 2;
        }break;
      case 2:
        State = "EJECTED";
        if (Altitude <= 510 && Altitude > 490){
          state = 3;
          S1r = 'R';
          Serial5.print("CMD,3751,SP1X,ON$");
          digitalWrite(Solinoid1,HIGH);
        }break;
      case 3:
        State = "RELEASED_1";
        digitalWrite(Solinoid1,LOW);
        if (Altitude <= 410 && Altitude > 390){
          state = 4;
          S2r = 'R';
          Serial4.print("CMD,3751,SP2X,ON$");
          digitalWrite(Solinoid2,HIGH);
        }break;
      case 4:
        State = "RELEASED_2";
        digitalWrite(Solinoid2,LOW);
        if (Altitude <= 5 && Altitude >= -5){
          state = 5;
          State = "LAND";
        }break;
      case 5:
        while (true){
          digitalWrite(buzzer,HIGH);
          delay(500);
          digitalWrite(buzzer,LOW);
          delay(500);
        }break;
    }
    Telemetry = teamId + "," + missionTime + "," 
       + String(Packet) + ",C," + Mode + "," + String(S1r) + ","
       + String(S2r) + "," + String(Altitude,2) + "," + String(Temp,2) + ","
       + String(Voltage) + "," + String(gpsTime) + "," 
       + String(Latitude,6) + "," + String(Longitude,6) + "," + String(gpsAltitude) + ","
       + String(gpsSatellite) + "," + State + "," + String(S1p) + ","
       + String(S2p) + "," + cmdEcho + "$";
    File file = SD.open(FileC, FILE_WRITE);
    if (file){
      file.println(Telemetry);
      file.close();
    }
    Serial.println("CX : " + Telemetry);
    Serial3.println(Telemetry);
    EEPROM.put(recovPkg, Packet);
    EEPROM.put(recovState, state);
    Packet ++;
    time0 = time1;
  }
}

void loop() {
  if (cxON){
    inMission();
  }
  if (Serial3.available()) {
    while (Serial3.available()){
      char inchar = Serial3.read();
      if (inchar =='$' or inchar == '\n'){
        cm = cm.trim();
        cm = (cm.substring(9));
        Serial.println("S3:" + cm);
        Command(cm);
        cm = "";
      }
      else{
        Serial.print(inchar);
        cm += inchar;
  }}}
  if(Serial5.available()){
    while (Serial5.available()){
      char inchar=Serial5.read();
      if (inchar=='$' or inchar=='\n'){
        S1=S1.trim();   
        Serial3.println(S1+"$");
        Serial.println("S1 : "+S1);
        S1p++;
        File file = SD.open(FileS1, FILE_WRITE);
        if (file){
          file.println(S1);
          file.close();
        }
        S1 = "";
      }
      else{
      S1+=inchar;
    }}}
  if (Serial4.available()){
    
    while (Serial4.available()){
      char inchar = Serial4.read();
      if (inchar == '$'){
        S2 = S2.trim();
        Serial3.println(S2 + "$");
        Serial.println("S2:" + S2);
        delay(100);
        S2p++;
        File file = SD.open(FileS2, FILE_WRITE);
        if (file){
            file.println(S2);
            file.close();
        }
        S2="";
      }
      else{
        S2 += inchar;
      }}}
}
