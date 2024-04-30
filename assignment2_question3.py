import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

tow = np.arange(-3, 0, 0.1)

x = cn.zpk2tf([-5], [0, -2, -4], 1)

G = cn.tf(x[0], x[1])

cn.rlocus(G)

plt.plot(tow, -tow * np.tan(np.arccos(0.5)))

s = - 0.8892 + 1.54j

K = cn.evalfr(-1/G, s)

print(K)

K = 2.66

t = np.arange(0, 10, 0.01)

clsys = K * G / (1 + K * G)
plt.figure()
cn.pzmap(clsys)
plt.figure()

y, T = cn.step(clsys, t)
def find_ts(t,y):
    i = y.size - 1
    while(True):
        if (y[i] - 1) ** 2 > (0.02) ** 2:
            ts = t[i]
            return ts
            break
        else:
            i = i - 1

def find_tr(t,y):
    i = 0 # soldan basliyiriq
    while(True):
        if (y[i]) > 1.00:
            tr = t[i]
            return tr
            break
        else:
            i = i + 1

y_max_index = np.argmax(y)
tp = t[y_max_index]
mp = y[y_max_index] - 1
tr = find_tr(t,y)
ts = find_ts(t,y)

plt.plot(t,y, label = f'Ts: {ts:.4f}, Tr: {tr:.4f}, Tp: {tp:.4f}, Mp: {mp:.4f}')
plt.legend()

x = cn.zpk2tf([], [-0.8892 + 1.54j, - 0.8892 - 1.54j], 0.8892**2 + 1.54**2)
Gs = cn.tf(x[0], x[1])
y, T = cn.step(Gs, t)

def find_ts(t,y):
    i = y.size - 1
    while(True):
        if (y[i] - 1) ** 2 > (0.02) ** 2:
            ts = t[i]
            return ts
            break
        else:
            i = i - 1

def find_tr(t,y):
    i = 0 # soldan basliyiriq
    while(True):
        if (y[i]) > 1.00:
            tr = t[i]
            return tr
            break
        else:
            i = i + 1

y_max_index = np.argmax(y)
tp = t[y_max_index]
mp = y[y_max_index] - 1
tr = find_tr(t,y)
ts = find_ts(t,y)
print(tr)
print(ts)
print(mp)
print(tp)


plt.plot(t,y, label = f'Ts: {ts:.4f}, Tr: {tr:.4f}, Tp: {tp:.4f}, Mp: {mp:.4f}')
plt.legend()

plt.show()
