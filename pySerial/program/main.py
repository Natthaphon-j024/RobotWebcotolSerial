# import serial
import time
import Serialmodule.Serialport as ser

from flask import Flask, render_template , request, jsonify
# from flask_cors import CORS

app = Flask(__name__)
# import Serial.Serialport as Serialport  # Removed as it could not be resolved
global Arduino 
# def main():
   
#     if Arduino is None:
#         Getserialport = ser.GetSerialPort()
#         print(Getserialport)
#         inputrKey = int(input("Select Serial Port:"))

#         if  inputrKey <= len(Getserialport):
#             print("Ok select a valid serial port.")
#             Arduino =  ser.SelectSerPort(Getserialport[0])
#         else:
#             print("Please select a valid serial port.")
#     # while True:
#     # ser.loop(Arduino)
#     return Arduino      
      
@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/readSerialPort', methods=['GET'])
def readSerialPort():
    
    if request.method == 'GET':
        Getserialport = ser.GetSerialPort()
        return {'status': 'success', 'port': '{}'.format(Getserialport)}, 200
@app.route('/selectSerialPort', methods=['POST'])
def selectSerialPort():
    if request.method == 'POST':
        port = request.json.get('port')
        print(port)
        Arduino = ser.SelectSerPort(port)
        return {'status': 'success', 'port': '{}'.format(Arduino)}, 200
    
    
    
    
@app.route('/updateValue' ,  methods=['POST' , 'GET'])
def updateServo():
    if request.method == 'POST':
        value = request.json.get('value')
        print(value)
        setArduino =  ser.SelectSerPort("COM6")
        print(setArduino)
       
        # Here you would typically send the value to the Arduino or process it as needed
        # For example: arduino.write(value.encode())
        
        return ser.UpdateServo(setArduino, value)
    elif request.method == 'GET':
        return { "value": "Get" }, 200

#arduino = serial.Serial(port='COM6',   baudrate=9600, timeout=.1)


# def write_read(x):
#     arduino.write(bytes(x,   'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return   data


# while True:
#     num = input("Enter a number: ")
#     value   = write_read(num)
#     print(value)
if __name__ == "__main__":
    # main()
    app.run()
    # pass  # This is where you would typically run your main function or script logic.
    