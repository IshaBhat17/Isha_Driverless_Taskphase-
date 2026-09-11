import csv
S=[]
def create():
    f1=open("cones.csv","a",newline="")
    n=int(input("Enter the number of entries "))
    w1=csv.writer(f1)
    for i in range(0,n):
        temp=[]
        id=int(input("Enter the id of the cone "))
        x=int(input("Enter the x coordinate "))
        y=int(input("Enter the y coordinate "))
        colour=(input("Enter colour blue/yellow ")).lower()
        temp=[id,x,y,colour]
        S.append(temp)
        w1.writerow(temp)   # bc we only want to input one row at a time 
    f1.close()
    print(S)

def sort():
    f1=open("cones.csv","w",newline="")
    w1=csv.writer(f1)
    for i in range(0,len(S)):
            m_index = i
            for j in range(i+1,len(S)):
                d1=(((S[j][1])**2) + ((S[j][2])**2))
                d2=(((S[m_index][1])**2) + ((S[m_index][2])**2))
                if d2 > d1:
                    m_index=j
            t=S[m_index]
            S[m_index]=S[i]
            S[i]=t
    for i in range(0,len(S)):  # bc we want csv to store it in diff rows 
        w1.writerow(S[i])
    f1.close()
    print(S)

def colour():
    f2=open("Blue.csv","w",newline="")
    w2=csv.writer(f2)
    f3=open("Yellow.csv","w",newline="")
    w3=csv.writer(f3)
    for i in range(0,len(S)):
        if S[i][3] =="yellow":
            w3.writerow(S[i])
        if S[i][3] =="blue":
            w2.writerow(S[i]) 
    f2.close()
    f3.close()

def mid_point():
    f2=open("Blue.csv","r",newline="")
    R2=csv.reader(f2)
    T1=list(R2)
    f2.close()
    f3=open("Yellow.csv","r",newline="")
    R3= csv.reader(f3)
    T2=list(R3)
    f3.close()
    f4=open("centreline.csv","w",newline="")
    w4=csv.writer(f4)
    for i in range(0,len(T1)):
        min_d=float('inf')
        for j in range(0,len(T2)):
            d=((int(T1[i][1]) - int(T2[j][1]))**2 + (int(T1[i][2]) - int(T2[j][2]))**2)**(1/2)
            if d<min_d:
                min_d=d
                n_y = T2[j]
        mid_x = (int(T1[i][1])+int(n_y[1]))/2
        mid_y = (int(T1[i][2])+int(n_y[2]))/2
        mid=[mid_x,mid_y]
        print("Blue:", T1[i])
        print("Nearest Yellow:", n_y)
        print("Midpoint:", mid)
        w4.writerow(mid)
    
    
    f4.close()
    f4=open("centreline.csv","r",newline="")
    R4=csv.reader(f4)
    for r in R4:
        print(r)
    f4.close()

create()
sort() 
colour()
mid_point()


    


        



       










