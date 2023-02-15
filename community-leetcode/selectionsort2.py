class Solution: 
  
    def select(self, arr, i):
        for i in range(len(arr)):
            small = i
            for j in range(i+1,len(arr)):
                if arr[small] > arr[j]:
                    small = j
        return arr[small]
    
    def selectionSort(self, arr,n):
        for i in range(n):
            small = i
            for j in range(i+1,n):
                if arr[small] > arr[j]: 
                    small = j
   
            (arr[i],arr[small])= (arr[small],arr[i])
                    
