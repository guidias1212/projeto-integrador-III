import serial
import requests

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()
url = 'http://localhost:8000/send_temp'

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        # myobj = {'temp': float(line)}
        myobj = {'temp': float(line)}
        x = requests.post(url, json = myobj)
        print(x.text)