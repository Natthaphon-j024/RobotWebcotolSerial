void setup() {
  // put your setup code here, to run once:

Serial.begin(9600);
Serial.println("Hello  Serial");
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN,1);
}

void loop() {
  // put your main code here, to run repeatedly:
String rawDataSerial =  "";
 if (Serial.available() > 0 ){
 rawDataSerial =  Serial.readString();
 rawDataSerial.trim();
 Serial.println("read  Serial  :  "+ rawDataSerial);
  Serial.println("read Serial if 90==input  :  "+ String(bool(String(rawDataSerial) == "90")));
   Serial.println("read Serial if 90==input  :  "+ String(bool("90" == "90")));
 }

 if (String(rawDataSerial)  == "90"){
  Serial.println("read Serial else  :  "+ rawDataSerial);
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
 }

 delay(300);

}
