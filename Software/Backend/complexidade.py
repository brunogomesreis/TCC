import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import datetime
from scipy.fftpack import fft
from scipy import signal 


N = 6000                 #Numero de pontos
T = 0.05                #Taxa de amostragem
x = np.linspace(0.0, N*T, N)
y1 = x**2
y2 = x*np.log10(x)

plt.figure()
plt.ylim(0,2000)
plt.xlabel("Dados de entrada")
plt.ylabel("Tempo de execução")

plt.plot(x,y1,color='red', label='O(n²)')
plt.plot(x,y2,color='blue', label='O(nlog(n))')
plt.legend()
plt.show()