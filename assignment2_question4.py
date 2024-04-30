import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 15, 0.01)

x = cn.zpk2tf([-5], [-1, -2, -4], 1)

G = cn.tf(x[0], x[1])

# Kp = 6
#
# Ki = 4
#
# Kd = 3

Kp = 5.7

Ki = 4.5

Kd = 2.9

Controller = cn.tf([Kd, Kp, Ki], [1, 0])

clsys = Controller * G / (1 + Controller * G)

y_step, T = cn.step(clsys, t)
def find_ts(t,y):
    i = y.size - 1
    while(True):
        if (y[i] - 1) ** 2 > (0.02) ** 2:
            ts = t[i]
            return ts
            break
        else:
            i = i - 1

y_max_index = np.argmax(y_step)
tp_step = t[y_max_index]
mp_step = y_step[y_max_index] - 1
ts_step = find_ts(t,y_step)

plt.plot(t, y_step, label = 'ts (step) =' + str(ts_step) + ', Mp (step) =' + str(mp_step))
plt.legend()
plt.figure()

y_ramp, T, x = cn.lsim(clsys, t, t)
plt.plot(t, t)
plt.plot(t, y_ramp)
plt.show()

