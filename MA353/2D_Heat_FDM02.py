import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

print("Start : . . .")
print("........................")
print("Solution of 2D Heat Equation")
print("........................")

w, h = input("Define your domain's width and height").split()
print(f"Width = {w} x Height = {h}")

plate_width = int(w) #ความกว้าง
plate_height = int(h) #ความยาว

it = input("Define number of iterations : ")
max_iter_time = int(it) #วนลูป ทำงานมากสุด 500 รอบ

nx = 101
ny = 101

alpha = 2
delta_x = plate_width/(nx-1)
delta_y = plate_height/(nx-1)

delta_t = (delta_x ** 2)/(4 * alpha)
gamma = (alpha *delta_t)/(delta_x ** 2)

#initialize the solution: the grid of u(k,i,j) #kจำนวนรอบ
u = np.empty((max_iter_time,ny,nx ))
#print(np.zeros((10,5)))

# initail condition everywhere inside the grid
u_initial = 0
#u_initial = np.random.uniform(low=28.5, high=55.5, size=(plate_width, plate_hight))

# boundary contitions:
u_top = 0.0
u_bottom = 0.0
u_left = 100.0
u_right = 0.0


#set the initial condition
#u[0, :, :] = u_initial
u.fill(u_initial)

# set boundary conditions
u[:, -1:,  :] = u_top
u[:,   :1, :] = u_bottom
u[:,   :,  :1] = u_left
u[:,   :,  -1:] = u_right

# define a function to calculate the solution
# of each time  k

def calculate(u): #คำนวนค่า
    for k in range(0, max_iter_time -1, 1): #เริ่มจาก0-499 ไปทีละ1
        for i in range(1, ny -1, 1): #iความสูงเริ่ม1-49 ที่ละ1
            for j in range(1, nx -1 , 1): #jความสูงเริ่ม1-49 ที่ละ1
                u[k + 1, i, j] = u[k][i][j] + gamma * (u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j])
    return u

def plot_haet_map(u_k, k): #สี
    # clear the current figure
    plt.clf()
    
    plt.title(f'Temperature at t = {k * delta_t:.3f} unit time')
    plt.xlabel("x")
    plt.ylabel("y")
    
    #plot u_k (u  at time_step k)
    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)
    plt.colorbar
    
    return plt


# do the calculation here
u = calculate(u)

def animate(k):
    plot_haet_map(u[k], k)
    
anim = FuncAnimation(plt.figure(), animate, interval=1, frames=max_iter_time, repeat=False)
anim.save("solution_of_2d_haet_eq.gif")

#animate(300)

plt.show()

print("Done !!")
