
import numpy as np 
from scipy.optimize import minimize

v_i = 5.5
v_d = 10 
x_i = 0.1
y_i = 3.1
H_i = np.deg2rad(90)
a_i = 1.3
w_i = 0.23
dt = 0.02
N = 3
A = np.array([0.9, 3.0])
B = np.array([1.0, 4.1])    # nearest way point 
H_d = np.atan2(B[1] - A[1], B[0] - A[0])

def position(a, w):
    x = x_i
    y = y_i
    H = H_i
    v = v_i
    # we initialise all these variables again bc everytime the optimiser calls the function the cars position should be at the beginning
    Pos = []
    for i in range(N):
        x = x + v * np.cos(H) * dt
        y = y + v * np.sin(H) * dt
        v = v + a * dt 
        H = H + w * dt 
        Pos.append([x, y, v, H])
    return Pos

def cost_function(opt):
    a = opt[0]
    w = opt[1]
    # we do this bc scipy sends both a and w as a list ... so both are sent together 
    p = position(a, w)
    # cross track error
    J_h = J_c = J_v = 0  
    for x, y, v, H in p:
        # heading error 
        H_diff = H_d - H
        H_e = np.arctan2(np.sin(H_diff), np.cos(H_diff))
        # we do this in order to keep the angle range from- 180 to +180. 
        # what we do is , we find the difference in the angle and then find the sin and cos function of it 
        # the sin function gives the y length and cos function gives the x length 
        # then we use atan2 to find the angle betwee the 2. this angle is the error 

        # cross track error 
        d_e = (abs((B[0]-A[0])*(A[1]-y) - (B[1]-A[1])*(A[0]-x))) / np.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)
       
        # velocity error 
        v_e = v_d - v 

        J_h += H_e**2 
        J_c += d_e**2 
        J_v += v_e**2

    # weights - change these values during trial and error
    w_h = 1
    w_c = 0.3
    w_v = 0.2

    J = w_h*J_h + w_c*J_c + w_v*J_v
    return J

# Initial cost before optimisation
J_initial = cost_function([a_i, w_i])

# Bounds for acceleration and yaw rate
bounds = [(-13, 13), (-1.3, 1.3)]

# result = minimize(function u wanna minimise, initial guess)
result = minimize(cost_function,[a_i, w_i], bounds=bounds   )

a_opt = result.x[0]   # optimal value of our variable 
w_opt = result.x[1]
J_opt = result.fun   # returns the minimum cost 

print("Initial cost:", J_initial)
print("Optimal acceleration:", a_opt)
print("Optimal yaw rate:", w_opt)
print("Optimised cost:", J_opt)
print("Optimisation successful:", result.success)  # tells if the code is successful
print("Message:", result.message)
