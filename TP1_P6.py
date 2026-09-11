n=int(input("Enter the number of elements "))
h_t= []
for i in range(10):
    h_t.append([])

for i in range(0,n):
    v=int(input("Enter the number "))
    
    index = v % 10
    A=h_t[index]

    low =0
    high = len(A) - 1
    
    while low <=high:
        mid = (low + high) // 2
        if A[mid]<v:
            low = mid + 1
        else:
            high = mid - 1
    
    h_t[index].insert(low,v)

for i in range(0,10):
    print(i,":",h_t[i])     