class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        answer = 0
        if n < 3 : 
            return answer
        
        start,end = 1,1
        for i in range(1,n-1):
            
            start= end = i 
            if arr[start-1] >= arr[i] or arr[end+1] >= arr[i]:
                continue
            
            while start > 0:
                if arr[start-1] < arr[start]:
                    start -=1
                else:
                    break
            
            while end < n-1:
                if arr[end+1] < arr[end]:
                    end+=1
                else:
                    break
            answer = max(answer,end-start +1)
        
        return answer
