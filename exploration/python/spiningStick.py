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
    
# Signal Generator
"""
A =  2# Period
a = 1 # Square signal width
x1 = np.arange(-20,20,0.1)
y1 = a*np.sinc(x1)
plt.grid(b=True, which='both', color='0.65',linestyle='-')
x = linspaceFourierSeries(20,a,A)
y = a*np.sinc(x)
plt.plot(x,y,'ro',x1,y1)
plt.show()


print "hoahoaholllholahola"
"""
fig2,ax = plt.subplots()

line, = ax.plot([],[],'ro-')
ax.grid
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)

def functionAnimation(x):
    np.sinc(x)
    return x
def data_gen(t=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.1
        yield t
def init():
    line.set_data([0,0],[0,1])
    return line
def animate(i):
    line.set_data([0,np.cos(0.01*i)],[0,np.sin(0.01*i)])
    return line

ani = animation.FuncAnimation(fig2,animate,data_gen,interval=20,init_func=init)
plt.show()
