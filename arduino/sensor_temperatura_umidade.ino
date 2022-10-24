#include <DHT.h>
#include <Ethernet.h>
#include <SPI.h>

byte mac[] = { 0x00, 0xAA, 0xBB, 0xCC, 0xDE, 0x01 };
EthernetClient client;

#define DHTPIN 6
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

long milisegAnterior = 0;
unsigned long milisegAtual = 0;
long intervalo = 250000;

int t = 0; // variavel para guardar temperatura
int h = 0; // variavel para guardar umidade
String data;

void setup() {
Serial.begin(115200);

pinMode(7, OUTPUT);      // seleciona o pin 7 do Arduino como output de informacoes de temperatura
pinMode(5, OUTPUT);      // seleciona o pin 5 do Arduino como output de informacoes de umidade
digitalWrite(7, HIGH);
digitalWrite(5, LOW);

if (Ethernet.begin(mac) == 0) {
Serial.println(“Houve algum erro de conexao com a internet”);
}

dht.begin();
delay(10000); // aguardar 10 segundos para o sensor iniciar

h = (int) dht.readHumidity(); // ler sensor de umidade inicial
t = (int) dht.readTemperature(); // ler sensor de temperatura inicial

data = “”; // variavel que ira guardar as informacoes dos sensores
}

void loop(){ // inicio do loop infinito que ficara lendo as informacoes dos sensores e enviando para o servidor

milisegAtual = millis();
if(milisegAtual – milisegAnterior > intervalo) { // Ler sensores dentro do intervalo selecionado no looping
milisegAnterior = milisegAtual;
h = (int) dht.readHumidity(); // ler sensor de umidade
t = (int) dht.readTemperature(); // ler sensor de temperatura
}

data = “temperatura=”;

data.concat(t); // adicionar leitura de temperatura na variavel que sera enviada para base de dados

data.concat(“&umidade=”);

data.concat(h); // adicionar leitura de umidade na variavel que sera enviada para a base de dados

if (client.connect(“https://projeto-integrador-poc.herokuapp.com”,80)) { // hostname do servidor em nuvem
client.println(“POST /sensor HTTP/1.1”); // endpoint tipo POST do metodo que ira salvar na base de dados
client.println(“Host: https://projeto-integrador-poc.herokuapp.com”); // mostrar nos logs o nome do hostname do servidor na nuvem
client.println(“Content-Type: application/x-www-form-urlencoded”);
client.print(“Content-Length: “);
client.println(data.length());
client.println();
client.print(data);
}

if (client.connected()) {
client.stop(); // desconectar do servidor
}

delay(300000); // esperar 5 minutos antes de enviar uma nova requisicao