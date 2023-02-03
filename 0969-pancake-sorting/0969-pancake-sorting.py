class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []
        for i in range(len(arr)-1,0,-1):
            maxindex = 0
            for i in range(1,len(arr[:i+1])):
                if arr[i] > arr[maxindex]:
                    maxindex = i
            
            if maxindex != i:
                start,end = 0,len(arr[:maxindex+1])-1
                while start < end :
                    arr[start],arr[end]  = arr[end],arr[start]
                    start +=1
                    end -=1
                answer.append(maxindex+1)
                
                start,end = 0,len(arr[:i+1])-1
                while start < end :
                    arr[start],arr[end]  = arr[end],arr[start]
                    start +=1
                    end -=1
                answer.append(i+1)
           
        return answer
        