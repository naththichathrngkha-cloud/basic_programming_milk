# 1-Dimension Heat Trandfer
# u_t = alpha + u_xx
# B.C. : u(0,t) = a , u(n,t) = b ; t>0
# I.C. : u(x,0) = f(x) ; 0<x<n 

import numpy as np
import matplotlib.pyplot as plt 
from math import pi
from sympy import * 

alpha = 0.2
L = 2 * np.pi                   #ความยาวของโดเมน
n = 100                  #แบ่งโดเมนเป็น 10 ส่วนเท่าๆกัน
t_final = 1          #เวลาที่ต้องการ n วิ

dx = L/n
dt = 0.5 * dx**2 / alpha   
N = int(t_final / dt)          #จำนวนรอบ

#Dirichlet Boundary Condition :

# B.C. : u(0,t) = 0 , u(n,t) = 0 ; t>0    #เงื่อนไขค่าขอบ
u_0t = 0
u_nt = 0

# I.C. : u(x,0) = 100 ; 0<x<n    #เงื่อนไขเริ่มต้น 
#x = np.zeros(n+1)
#u = np.linspace(0, L, n+1)

#หา x**3
# I.C. : u(x,0) = 100 ; 0<x<L 
x = np.linspace(-L, L, n+1)
u = x**3


#u = np.ones(n+1) * u_x0                    #ค่าเริ่มต้น

u[0] = u_0t                               #u ตัวแรก
u[-1] = u_nt                              #u ตัวสุดท้าย 

 
for j in range(1,N+1):
    w = u.copy()                   # u เก็บไว้ใน w ดังนั้น w จะหน้าตาเหมือน u 
    for i in range(1,n) :
        u[i] = w[i] + alpha * dt *((w[i+1] - 2*w[i] + w[i-1])/dx**2)
    print(f"Round {j} : {u}")
    plt.clf()                      #ให้กราฟที่ plot แล้วหายไป แล้ว plot กราฟใหม่
    plt.xlim(-L, L)
    plt.ylim(-100, 100)                     
    plt.plot(x,u)
    #plt.title(f"Distribuion at Round {j} ")
    #plt.title(f"Distribuion at time {j*dt} ")
    #plt.title("Distribuion at time {:.4f} ".format(j*dt))
    plt.title('Distribution at time  {:.4f} [s]'.format(j*dt))
    plt.pause(0.01)        #เวลาในการplotกราฟแต่ละรอบ

plt.show()
    
    