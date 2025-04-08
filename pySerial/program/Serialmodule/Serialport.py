import serial.tools.list_ports
import time
def  GetSerialPort():
     # Get a list of available serial ports
    PortsList = []
    ports = serial.tools.list_ports.comports()
    # Print each port
    for port in ports:
        print(port.device)
        PortsList.append(port.device)
    return  PortsList

def  SelectSerPort(portSelect):
    
    arduino = serial.Serial(port='{}'.format(portSelect),   baudrate=9600, timeout=.1)
    return arduino

def write_read(fuArduino,  x):
    arduino = fuArduino
    arduino.write(bytes(x,   'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return   data

def loop(Arduino): 
    # while True:
    num = input("Enter a number: ")
    value   = write_read(Arduino , num)
    print(value)
    
def UpdateServo(Arduino, value):
    # Here you would typically send the value to the Arduino or process it as needed
    # For example: arduino.write(value.encode())
    write_read(Arduino , value)
    return {'status': 'success', 'value': value}
        
if __name__ == "__main__":
    # GetSerialPort()
    pass  # This is where you would typically run your main function or script logic.