def sort():
    for i in range(0,len(L)):
        m_index = i
        for j in range(i+1,len(L)):
            d1=int((((ref[0]-L[j][0])**2) + ((ref[1]-L[j][1])**2))**(1/2))
            d2=int((((ref[0]-L[m_index][0])**2) + ((ref[1]-L[m_index][1])**2))**(1/2))
            if d2 < d1:
                m_index=j
        temp=L[m_index]
        L[m_index]=L[i]
        L[i]=temp
    print(L)

n=int(input("Enter the number of coordinates "))
L=[]
for i in range(0,n):
    x=int(input("Enter the x coordinate"))
    y=int(input("Enter the y coordinate"))
    Cord = [x,y]
    L.append(Cord)

r_x=int(input("Enter the reference x coordinate"))
r_y =int(input("Enter the reference y coordinate"))
ref = [r_x,r_y] 
if ref in L:
    print("Enter again")
else:
    sort()









    