"""
Reads hearth electical signalsl
 Data provided by MIT-OCW

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# data = pd.read_csv('datafiles/normal.txt', sep = ' ', header = None)
def read_text():
    data = pd.read_table('datafiles/normal.txt', sep = ' ', skipinitialspace = True, header = None)
    data.columns = ['time', 'amplitude' ]
    data.set_index('time')
    return  data
def window(y ,t , time_shift, n_points, type = 'square'):
    for (index , time) in enumerate(t):
        if time > time_shift:
            start_index = index
            break
    windowed_out = np.array([y[start_index: start_index + n_points] ,
                            t[start_index: start_index + n_points]])
    return windowed_out[1,:] , windowed_out [0,:]

data = read_text()
y = np.array(data['amplitude'])
t = np.array(data['time'])

t_1, y_1 = window(y,t,10,10000)
plt.plot(t_1,y_1)

plt.title("ECG from normal patient")
plt.xlabel("tiempo [sec]")
plt.ylabel("mV")
plt.show()
