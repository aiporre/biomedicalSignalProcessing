# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:54:39 2016

@author: Ariel Iporre
"""
#%matplotlib inline 
import numpy as np
import matplotlib.pyplot as plt
#from __future__ import division

freq = 50.0
time_period = 1/freq
time = time_period*2
amplitude = 2

# Defining continuos function
t = np.linspace(0, time, 500, endpoint = True)
x = 2*np.pi*freq*t

yc = amplitude * np.sin(x) + 1*np.random.rand(len(x))

# Sampling
Fs = 20*50.0; 
Ts = 1/Fs
ts =np.arange(0,(time+Ts/2),Ts)
r = np.round(len(t)/len(ts))
xts = np.arange(0,len(t),r).astype('int')

xs = x[xts]
ys = yc[xts]

# Ploting

fig1 = plt.figure(figsize = (10,4))
axes1 = fig1.add_axes([0.1,0.1,0.8,0.8])

axes1.plot(x,yc,color = 'red', linewidth = 3, linestyle = '-')
axes1.plot(xs,ys,color = 'blue', linestyle = ' ', marker = 'o')
axes1.bar(xs,ys, bottom = 0, width = 0.02, color = 'blue')
axes1.axhline(0,color = 'black',  linestyle = '-', linewidth = 1)
axes1.set_ylim([-3,3])
axes1.set_xlim(0,np.max(x))


axes1.set_xticks((2*np.pi*freq)*np.arange(0,41,5)*1e-3);
axes1.set_xticklabels(np.arange(0,41,5),fontsize=14);
plt.show()

