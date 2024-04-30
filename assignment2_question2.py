import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 25, 0.01)

x = cn.zpk2tf([], [0, -3, -5], 1)

G = cn.tf(x[0], x[1])

plt.figure()
cn.rlocus(G)
plt.title('Root Locus of Open Loop System')


K_values = [2, 5, 8.21, 15, 30, 130]

for K in K_values:
    clsys = K * G / (1 + K * G)
    plt.figure()
    cn.pzmap(clsys)
    plt.title(f'Pole-Zero Map for K={K}')

    y, T = cn.step(clsys, t)

    def find_ts(t, y):
        i = y.size - 1
        while (True):
            if (y[i] - 1) ** 2 > (0.02) ** 2:
                return t[i]
                break
            else:
                i = i - 1

    ts = find_ts(t,y)

    print(ts)

    plt.figure()
    plt.plot(t,y, label = f'Settling time for K={K}: {ts:.2f} seconds')
    plt.legend()


plt.show()

