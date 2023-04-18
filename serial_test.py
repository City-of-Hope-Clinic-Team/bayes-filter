from math import sqrt
import serial

ser = serial.Serial('COM5', 115200)
ser.flushInput()

while True:
    ser_bytes = ser.readline()
    decoded_bytes = ser_bytes[0:len(ser_bytes)-1].decode("utf-8")
    str_list = decoded_bytes.split(",")
    output = [int(i) for i in str_list]
    energy = sqrt(output[0]**2 + output[1]**2 + output[2]**2)
    print(str(output)[1:-1], ",", round(energy,2))
    