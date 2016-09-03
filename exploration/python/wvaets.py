
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(-1, 1, 200, endpoint=False)
sig  = np.cos(2 * np.pi * 7 * t) + signal.gausspulse(t - 0.4, fc=2)
fig1,handler = plt.subplots()
handler.grid(True)
handler.plot(t,sig)
#

widths = np.arange(1, 31)
cwtmatr = signal.cwt(sig, signal.ricker, widths)
fig2,handler2 = plt.subplots()
plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
#handler2.plt.show()

plt.show()
