#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy as np
import math

def f(t) :
    return (t**2 + np.sin(t))


# F(t) es la integral, así que la calculamos
def F(t) :
    return (t**3 / 3) - np.cos(t) + 1



prev = 0
def approximation (t, tr) :
    global prev, percount
    if t == 0 :
        return 0
    r = 0
    i = t
    r = prev + tr / 2 * (f(i) + f(i - tr))    # Como es f[i-1], se resta un tr
    prev = r
    return r


trit = [0.1, 0.01, 0.001, 1e-4, 1e-5]
for tr in trit :
    N = int((np.pi / 2) // tr + 1)
    T = np.array([i*tr for i in range(N)])
    fy = np.array([f(T[i]) for i in range(N)])
    y = np.array([F(T[i]) for i in range(N)])
    yp = np.array([approximation(T[i], tr) for i in range(N)])

    err = np.abs(y - yp)

    print(f"Graficando {tr}...")
    plt.plot(T, err)
    plt.savefig(f"Error{tr}.png")
    plt.clf()
