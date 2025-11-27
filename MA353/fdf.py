import numpy as np
from sympy import *
#from math import pi
import math 
from matplotlib import pyplot as plt


x = Symbol("x")
y = (sin(5*x))**2 + exp(5*x)                     #ตัวแปรที่ต้องการใส่ฟังก์ชันในการ diff    

for i in range(6):
    y_dif = y.diff(x,i)
    print(f'{i} = {y_dif}')
    