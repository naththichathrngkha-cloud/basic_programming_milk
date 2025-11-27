import numpy as np
from sympy import *
#from math import pi
import math 
from matplotlib import pyplot as plt


x = Symbol("x")
y = x**5              #ตัวแปรที่ต้องการใส่ฟังก์ชันในการ diff  
a = 0    
'''                
y_0 = cos(a)                    
print(f'y_0 at a = 0 is {y_0}')       

y_1 = y.diff(x, 1)       
y_1 = lambdify(x, y_1)
print(f'y_1 = {y_1(a)}')       
 
y_2 = y.diff(x, 2)       
y_2 = lambdify(x, y_2)
print(f'y_2 = {y_2(a)}') 
'''
Tn = 0

for i in range(9):
    y_dif = y.diff(x,i)
    y_dif = lambdify(x, y_dif)
    #print(f' {i}: y_dif at a = 0 is {y_dif(a)}')
    Ti = y_dif(a)/math.factorial(i) * (x-a)**i
    Tn_i = Ti
    Tn = Tn + Tn_i
    print(f'{i}: = {Tn}')

Tnn = lambdify(x, Tn)
print(f'Tnn = {Tnn(math.pi)}')
x = np.linspace(-5, 5, 100)
plt.plot(x, Tnn(x))
plt.show()
    