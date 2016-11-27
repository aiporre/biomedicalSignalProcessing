import numpy as np
import matplotlib.pylab as plt
import padasip as pa
# creation of u, x and d
N = 100
u = np.random.random(N)
d = np.zeros(N)
for k in range(3, N):
    d[k] = 2*u[k] + 0.1*u[k-1] - 4*u[k-2] + 0.5*u[k-3]
d = d[3:]


# identification
x = pa.input_from_history(u, 4)
y, e, w = pa.rls_filter(d, x, mu=0.1)

# show results
plt.figure(figsize=(13,9))
plt.subplot(211);plt.title("Adaptation");plt.xlabel("samples - k")
plt.plot(d,"b", label="d - target")
plt.plot(y,"g", label="y - output");plt.legend()
plt.subplot(212);plt.title("Filter error");plt.xlabel("samples - k")
plt.plot(abs(e),"r", label="abs(e) - prediction error");plt.legend()
plt.tight_layout()
plt.show()