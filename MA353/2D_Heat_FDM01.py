import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation 


print("Solution of 2D Heat Equation")

plate_width = 50            #กว้าง
plate_hight = 50            #สูง

max_iter_time = 500                          #วนลูบ/ทำงานกี่รอบ

alpha = 2
delta_x = 1

delta_t = (delta_x **2)/(4 * alpha)
gamma = (alpha * delta_t)/(delta_x ** 2)

# initialize the solution: the grid of u(k,i,j)                         #เวลาที่ k ในตำแหน่ง i,j ใดๆ
u = np.empty((max_iter_time ,plate_width,plate_hight))

# initial condition everywhere inside the grid
#u_initial = 0
u_initial = np.random.unifrom(low=28.5, high=55.5, size=(plate_width,plate_hight))

# boundary contition :
u_top = 100.0
u_left = 0.0
u_right = 0.0
u_bottom = 0.0

# set the initial condition :
u[0, :, :] = u_initial                             #เอาทุกแถวทุกหลักในเวลาที่ 0 

# set boundary condition : 
u[ :, -1:,   : ]  = u_top
u[ :,   :1,  : ]  = u_bottom
u[ :,   :,   :1]  = u_left
u[ :,   :, -1: ]  = u_right

# define a function yo d=calculate the solution
# do each time k 


def calculate(u):
    for k in range(0, max_iter_time -1, 1):
        for i in range(1, plate_hight -1, delta_x):
            for j in range (1, plate_width -1, delta_x):               #วิ่ง j ครบทุกตัวแล้ว วิ่ง i แล้วค่อย วิ่ง k
                u[k + 1, i, j] = u[k][i][j] + gamma * (u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1]-4*u[k][i][j])
    return u 

def plot_heat_map(u_k, k):
    # clear the current figure
    plt.clf()
    
    plt.title(f'Temperature at t = {k * delta_t:.3f} unit time')
    plt.xlabel("x")
    plt.ylabel("y")
    
    # plot u_k (u at time-step k )
    plt.pcolormesh(u_k, cmap = plt.cm.jet, vmin=0,vmax=100)
    plt.colorbar
    
    return plt

# do the calculation here
u = calculate(u) 

def animate(k):
    plot_heat_map(u[k], k)
    
anim = FuncAnimation(plt.figure(), animate, interval=1, frames=max_iter_time, repeat=False)
anim.save("solution_to_2d_heat_eq.gif")

plt.show()

print("Done !!")    
    