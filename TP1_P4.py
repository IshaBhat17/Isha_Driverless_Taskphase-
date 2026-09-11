n=int(input("Enter the number of rows in matrix 1 "))
m=int(input("Enter the number of column in matrix 1 "))
p=int(input("Enter the number of rows in matrix 2 "))
q=int(input("Enter the number of column in matrix 2 "))
L=[]
M=[]
N=[]
if(m!=p):
    print("Matrix multiplication is not possible")

else:
    
    for i in range(0,n):
        row=[]
        for j in range(0,m):
            v=int(input("Enter the elements of matrix 1 "))
            row.append(v)
        L.append(row)



    for i in range(0,p):
        row=[]
        for j in range(0,q):
            v=int(input("Enter the elements of matrix 2 "))
            row.append(v)
        M.append(row)


    for i in range(0,n):
        row=[]
        for j in range(0,q):
            row.append(0)
        N.append(row)

    for i in range(0,n):
        for j in range(0,q):
            S=0
            for k in range(0,m):
                S +=L[i][k]*M[k][j]
            N[i][j]=S
    for i in range(0,n):
        for j in range(0,q):
            print(N[i][j],end=" ")
        print()

       
        

