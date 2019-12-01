import serial
import time
import csv
import asyncio

class BreathHardwareController:
    
    _instance = None
    _start = False

    ser = serial.Serial('COM6', 9600)
    ser.flushInput()

    def __new__(self):
        if not self._instance:
            self._instance = super(BreathHardwareController, self).__new__(self)
        return self._instance

    async def startBreathMeasure(self,directory):
        self._start = True
        while self._start:
            try:
                ser_bytes = ser.readline()
                try:
                    decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                    print(decoded_bytes)
                    tempo = time.asctime( time.localtime(time.time()) )    
                except:
                    continue
                with open(directory + "Medição.csv","a") as f:
                    writer = csv.writer(f,delimiter=",")
                    writer.writerow([time.time_ns(),decoded_bytes]) 

    # async def stopBreathMeasure(self):
    #     self._start = False