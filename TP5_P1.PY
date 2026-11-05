import numpy as np 
x = 10.0
y = 5.0
H1 = np.deg2rad(30)
T=0.2 
u=5.0
a=1.0
w=np.deg2rad(10)
H= H1+w*T  # calculating the final heading 
dt = 0.001
N = int(T/dt)
for i in range(N):  # loop is used to divide 0.2s into 200 parts
    t=i*dt  # used to calculate the time interval  
    v = u+a*t # change in velocity where v is the speed at that time
    H2 = H1+w*t     #change in heading where H2 is the heading at that time
    # both v and H2 are inside loop because we need them for each time interval 
    vx = v*np.cos(H2)   
    vy = v*np.sin(H2) 
    x =x+vx*dt  # we do dt here bc we are adding only the distance covered by the car in the next interval and not from the start 
    y =y+vy*dt    
print("New x :",x)
print("New y: ",y)
print("New heading: ",np.rad2deg(H),"degree")

cones = {"B1":[12,7],"B2":[8,6],"Y1":[13,4],"Y2":[9,3]}
xi = 10.0
yi = 5.0
Hi = np.deg2rad(30)
# for cones from initial position 
for C , [X,Y] in cones.items():   # X , Y are position of cones
    dx = X - xi 
    dy = Y- yi   # we do this to change the origin 
    xc = dx*np.cos(Hi) + dy*np.sin(Hi)
    yc = -dx*np.sin(Hi) + dy*np.cos(Hi)
    print(C ,":", xc , yc)

# for cones from changed postion 
for C , [X,Y] in cones.items():   # X , Y are position of cones
    dx = X - x 
    dy = Y- y   # we do this to change the origin 
    xc = dx*np.cos(H) + dy*np.sin(H)
    yc = -dx*np.sin(H) + dy*np.cos(H)
    print(C ,":", xc , yc)

# we can do the angle rotation using matrix multiplication as well
# # @ is used to multiply two matrices. 
# # example we wannna multiply matrix A and B ; R = A @ B 
#     

