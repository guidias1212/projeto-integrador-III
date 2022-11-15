#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>

void setup() {

  Serial.begin(115200);                 //Serial connection
  WiFi.begin("NET_2G2E5168", "2F2E5168");   //WiFi connection

  while (WiFi.status() != WL_CONNECTED) {  //Wait for the WiFI connection completion

    delay(500);
    Serial.println("Waiting for connection");

  }

}

void loop() {

  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status

    HTTPClient http;    //Declare object of class HTTPClient

    http.begin("http://localhost:8000/send_temp");      //Specify request destination
    http.addHeader("Content-Type", "application/json");  //Specify content-type header

    int httpCode = http.POST("{'temp':1212}");   //Send the request

    String payload = http.getString();                  //Get the response payload

    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload

    http.end();  //Close connection

  } else {

    Serial.println("Error in WiFi connection");

  }

  delay(30000);  //Send a request every 30 seconds

}