n=int(input("Enter the number of elements"))
h_t= []
for i in range(10):
    h_t.append([])

for i in range(0,n):
    v=int(input("Enter the number"))
    
    index = v % 10
    h_t[index].append(v)

for i in range(0,10):
    print(i,":",h_t[i])