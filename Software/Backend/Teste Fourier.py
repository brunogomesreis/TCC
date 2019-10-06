from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np
import datetime
import scipy.interpolate as interpolate
from sympy import symbols
import os
import time



# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)


datas = ['22:00:24.509','22:00:25.527','22:00:26.512','22:00:27.526','22:00:28.511','22:00:29.529','22:00:30.515','22:00:31.532','22:00:32.519','22:00:33.536','22:00:34.520','22:00:35.538','22:00:36.526','22:00:37.548','22:00:38.530','22:00:39.547','22:00:40.533','22:00:41.555','22:00:42.538','22:00:43.560','22:00:44.548','22:00:45.568','22:00:46.555','22:00:47.542','22:00:48.559','22:00:49.572','22:00:50.561','22:00:51.573','22:00:52.554']
y = [1023,1023,1022,1023,1023,1023,1023,1022,1023,1022,1023,1023,997,1007,1022,1009,1006,1016,1023,1012,997,1003,1013,1003,985,993,1008,1018,1023]
delta = GetDeltaTime(datas)
x = ConvertListOfDeltaToListOfSeconds(delta)






plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()