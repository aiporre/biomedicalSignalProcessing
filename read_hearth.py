"""
Reads hearth electical signalsl
 Data provided by MIT-OCW

"""
import pandas as pd
import matplotlib.pyplot as plt

# data = pd.read_csv('datafiles/normal.txt', sep = ' ', header = None)
data = pd.read_table('datafiles/normal.txt', sep = ' ', skipinitialspace = True, header = None)
data.columns = ['time', 'amplitude' ]
data.set_index('time', inplace = True)
print "Read data -------------->>>"
print data.head()

data.plot()


plt.title("ECG from normal patient")
plt.xlabel("tiempo [sec]")
plt.ylabel("mV")
plt.show()