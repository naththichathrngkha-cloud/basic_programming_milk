import numpy as np
import matplotlib.pyplot as plt 
from math import pi
from sympy import * 

alpha = 1.8
L = 3*np.pi 
n = 50 
t_final = 1

dx = L/n 
dt = 0.5 * dx**2 /alpha
N = int(t_final/dt)

#B.C. : w(0,t) = w(3*np.pi) = 15
x = np.linspace(0, L, n+1)
w = 108 * np.cos(x)

#I.C. : w(x,0) = 108*cos(x)
w_0t = 15
w_nt = 15 


w[0]  = w_0t
w[-1] = w_nt

for j in range(1, N+1):
    p = w.copy()
    for i in range(1, n):
        w[i] = p[i] + alpha * dt *((p[i+1] - 2*p[i] + p[i-1])/dx**2)
    plt.clf()
    plt.xlim(0, L)
    plt.ylim(-100, 100)
    plt.plot(x,w)
    plt.title('Distribution at time {:.4f} [s] '.format(j*dt))
    plt.pause(0.01)
    
plt.show()