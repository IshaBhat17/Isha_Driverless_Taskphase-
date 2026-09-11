class SelectionSort:
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

Q1=eval(input("Enter a list of elements"))
obj = SelectionSort(Q1)
print(obj.sort())   