"""
Course: Quaternion Wavelets in Medical signal processing

Example1_From Fourier series to Fourier transform
Description:
This example that shows how the fourier series exentends
its applicability for infinte periodic signals.

@autor ArielIporre
"""

import numpy as np
from numpy import sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import scipy as sp
#import math

#(hashtags) n, coef, freq, phase
def linspaceFourierSeries(X,a,A):
    # X limint in frequency
    return np.arange(-X,X,a*np.pi/A)
# ******************************   
## Signal Generator
# ******************************

A =  2 # Period
a = 1  # Square signal width
x1 = np.arange(-20,20,0.1)
y1 = a*np.sinc(x1)

##plt.plot(x,y,'ro',x1,y1)
##plt.show()


# ******************************
## Canvas Configuration
# ******************************
fig2,ax = plt.subplots() # creates figure and handler
line, = ax.plot([],[],'ro') # creates line object
line2, = ax.plot(x1,y1,'b') # creates line object
ax.grid(True)

ax.set_xlim(-20,20)# Set limints
# ******************************
## Animation Funtions
# ******************************
def data_gen(t=1):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.8
        yield t
def init():
    line.set_data([],[])
    return line,line2
def animate(i):
    x = linspaceFourierSeries(20,a,i)
    y = a*np.sinc(x)
    line.set_data(x,y)
    return line,line2

ani = animation.FuncAnimation(fig2,animate,data_gen,interval=200,init_func=init)
plt.show()
