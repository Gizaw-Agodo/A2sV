class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        
        ans = 0
        if k >n :
            return ans
        
        sum = 0 
        start = 0 
        for i in range(n):
            sum += arr[i]
            if i-start+1 == k:
                if sum/k >= threshold:
                    ans +=1
                sum -=arr[start]
                start +=1
            

        return ans
