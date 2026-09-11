n=int(input("Enter the number of elements in a list "))
L1=eval(input("Enter a list of elements "))
k=[]
val=[]
for i in range(0,n):
    c=0
    v=""
    v=L1[i].lower()
    for j in range(0,len(v)):
        c=0
        if v[j] in k:
            pos=k.index(v[j])
            val[pos] += 1
        else: 
            c=c+1
            k.append(v[j])
            val.append(c)
D1=dict(zip(k,val))
print(D1)