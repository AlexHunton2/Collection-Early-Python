import serial

ser = serial.Serial('COM5', 9600, timeout=0)

ser.write(b'0') 