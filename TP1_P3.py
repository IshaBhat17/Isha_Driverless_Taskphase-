
class Search:
    def __init__(self,Q1):
        self.Q1=Q1

    def sort(self):
        
            for i in range(0,len(self.Q1)):
                min_index= i
                for j in range(i+1,len(self.Q1)):
                    if(self.Q1[min_index]>self.Q1[j]):
                        min_index=j
                temp = self.Q1[min_index]
                self.Q1[min_index] = self.Q1[i]
                self.Q1[i]=temp
            return self.Q1

    def binary(self,N):
        low= 0
        high = len(self.Q1)-1
        while low <=high :
            mid =(low+high)//2
            if(self.Q1[mid]==N):
                print("Element is found")
                print(mid)
                return
            elif(self.Q1[mid]>N):
                high=mid-1
            else:
                low=mid+1
        
        print("Element not found")

Q1=eval(input("Enter a list of elements"))
N=eval(input("Enter the number to be found"))
obj=Search(Q1)
print(obj.sort())
obj.binary(N)