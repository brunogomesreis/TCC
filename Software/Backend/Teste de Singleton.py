from flask import Flask, jsonify, request
from pymongo import MongoClient
import asyncio
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)


class Singleton:
    __instance = None
 
    @property
    def x(self):
        return self.__x
 
    @x.setter
    def x(self, value):
        self.__x = value
 
    @staticmethod
    def instance():
        if not Singleton.__instance:
            Singleton.__instance = Singleton()
        return Singleton.__instance


s1 = Singleton.instance()
s2 = Singleton.instance()

s1.x = 10
print ("S1:")
print (s1.x)
print ("S2:")
print (s2.x)

s2.x = 50
print ("S1:")
print (s1.x)
print ("S2:")
print (s2.x)

@app.route('/')
def home():
    return "Hello TCC", 200

if __name__ == '__main__':
    app.run(debug=True)