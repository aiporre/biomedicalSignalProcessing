import numpy as np
import matplotlib.pylab as plt
import padasip as pa
plt.style.use('ggplot')

# signals creation: u, v, d
N = 1000
n = 15
u = np.sin(np.arange(0, N/10., N/10000.))
v = np.random.random(N) - 0.5
d = u + v

# filtering
x = pa.input_from_history(d, n)[:-1]
d = d[n:]
u = u[n:]
y, e, w = pa.rls_filter(d, x, mu=0.95)

# error estimation
MSE_d = np.dot(u-d, u-d) / float(len(u))
MSE_y = np.dot(u-y, u-y) / float(len(u))

# results
plt.figure(figsize=(13,6))
plt.plot(u, "r:", linewidth=4, label="original")
plt.plot(d, "b", label="noisy, MSE: {}".format(MSE_d))
plt.plot(y, "g", label="filtered, MSE: {}".format(MSE_y))
plt.xlim(800,900)
plt.legend()
plt.tight_layout()
plt.show()