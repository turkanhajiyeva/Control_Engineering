import numpy as np
import matplotlib.pyplot as plt
import control as cn

def system_response(omega_n, zeta):
    clsys = cn.tf([omega_n * 2], [1, 2 * zeta * omega_n, omega_n * 2])
    t, y = cn.step_response(clsys, np.linspace(0, 25, 1000))
    return t, y

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

def find_parameters(t, y):
    Yss = y[-1]
    y_max_index = np.argmax(y)
    tp = t[y_max_index]
    mp = y[y_max_index] - 1
    tr = find_tr(t,y)
    ts = find_ts(t,y)
    return tr, ts, tp, mp

def plot(t, y, omega_n, zeta, tr, ts, tp, mp):
    plt.figure()
    plt.plot(t, y)
    plt.title(f'Step Response: wn={omega_n}, zeta={zeta}, ts={ts:.4f},tr={tr:.4f},tp={tp:.4f},Mp={mp:.4f})')
    plt.legend()
    plt.show()

def simulate(omega_n, zeta):
    t, y = system_response(omega_n, zeta)
    tr, ts, tp,  mp = find_parameters(t, y)
    plot(t, y, omega_n, zeta, tr, ts, tp, mp)

simulate(1, 0.2)
simulate(1, 0.4)
simulate(1, 0.6)

