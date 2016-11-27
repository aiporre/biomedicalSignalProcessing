
"""
Reads hearth electical signalsl
 Data provided by MIT-OCW

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import fft
import padasip as pa

# data = pd.read_csv('datafiles/normal.txt', sep = ' ', header = None)
def read_text():
    data = pd.read_table('datafiles/normal.txt', sep = ' ', skipinitialspace = True, header = None)
    data.columns = ['time', 'amplitude' ]
    data.set_index('time')
    return  data
def window(y ,t , time_shift, n_points, type = 'square')  :
    for (index , time) in enumerate(t):
        if time > time_shift:
            start_index = index
            break
    windowed_out = np.array([y[start_index: start_index + n_points] ,
                            t[start_index: start_index + n_points]])
    return windowed_out[1,:] , windowed_out [0,:]
def fourier_transform(y,sample_period):
    hat_y = fft.fft(y)
    frequency = fft.fftshift(fft.fftfreq(len(y),sample_period))
    return frequency, hat_y

data = read_text()
y = np.array(data['amplitude'])
t = np.array(data['time'])

t_1, y_1 = window(y,t,10,1024)
sample_period = t_1[1] - t_1[0] #TODO: use min distance instead
# f expressed in hertz and hat_y is fourier transform
freq, hat_y = fourier_transform(y_1, sample_period)

figure, ax = plt.subplots(2,1)
ax[0].plot(t_1,y_1)
ax[1].plot(freq, np.absolute(hat_y))

ax[0].set_title("ECG from normal patient")
ax[0].set_xlabel("tiempo [sec]")
ax[0].set_ylabel("mV")

# ax[1].set_title("ECG sprectrum")
ax[1].set_ylabel("spectrum")
ax[1].set_xlabel("frequency[Hz]")

plt.show()
