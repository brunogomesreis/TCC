from flask import Flask, jsonify, request
from pymongo import MongoClient
import asyncio
import time
#import BreathHardwareController
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)


class Singleton:
    __instance = None
    __x = False
    __i = 0

    @property
    def x(self):
        return self.__x
    def i(self):
        return self.__i

    @x.setter
    def x(self, value):
        self.__x = value
 
    @staticmethod
    def instance():
        if not Singleton.__instance:
            Singleton.__instance = Singleton()        
        return Singleton.__instance    

    # def startLoop():
    #     self.__x = True
    # def stopLoop():
    #     self.__x = False

    # while __x:
    #     print (__i)
    #     __i+=1
    #     time.sleep(10)

    def loop():
        while __x:
            try:
                ser_bytes = __i
                try:
                    print(decoded_bytes)
                except:
                    continue
                with open("test_data.csv","a") as f:
                    writer = csv.writer(f,delimiter=",")
                    writer.writerow([ser_bytes])
            except:
                print("Keyboard Interrupt")
                break







# @app.route('/start/<int:id_paciente>', methods=['GET'])
# def start(id_paciente):
#     patient = getPatient(id_paciente)     
#     createDirectory(patient)
#     directory = getLastPatientFolder()
#     startBreathMeasure(patient.directory, True)

# @app.route('/stop/<int:id_paciente>', methods=['GET'])
# def stop(id_paciente):
#     startBreathMeasure(id_paciente, False)

# @app.route('/getCsvFile/<int:id_medicao_csv>', methods=['GET'])
# def getCsvFile(id_medicao_csv):

# @app.route('/plotCsvFile/<int:id_medicao_csv>', method=['GET'])
# def plotCsvFile(id_medicao_csv):
#     medicao = getCsvFile(id_medicao_csv)



@app.route('/')
def home():
    return "Hello TCC", 200

@app.route('/Start')
def start():
    s1 = Singleton.instance()
    if not s1.x:
        s1.x = True        
        return "Iniciando Medição",200
    else:
        return "Medição já iniciada",200

@app.route('/Stop')
def stop():
    s1 = Singleton.instance()
    s1.x = False
    # print('s1.x={} | s2.x={}'.format(s1.x, s2.x))
    return 'Medição Finalizada i ={}'.format(s1.i),200



if __name__ == '__main__':
    app.run(debug=True)