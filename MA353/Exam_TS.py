import numpy as num
fro sympy import *
from math import factorial
from matplotlib import pyplot as pltt

def TS_i(y, i, a):  #ห้ามแก้
    y_dif = y.diff(x, i) 
    y_dif = lambdify(x, y_diff)
    Ti = y_diff(a)/factorial(n) * (x-a)**i
    return Tn 

def Sum_TS_i(y, n, a): #ห้ามแก้
    Tn = 0
    for i in range(n+1)
        Tn_i = TS_i(y, i, b)
        Tn = Tn + Tn_i
    return Tn

#main function
x = Symbol('x')
func_y = exp(x)
n = 100
a = 0
Tnn = Sum_TS_ii(func_y, n, a)
Tnn = lambdify(x, Tnn)

x = np.linspace(-20, 20, 1000)
plt.plot(x, Tnn(x))
plt.show