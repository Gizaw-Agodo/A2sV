class Solution:
   
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        maximum = float('-inf')
        memo = {}
        def getNums(n):
            nonlocal maximum
            if n == 1:
                return 1
            if n == 0:
                return 0
           
            if n not in memo:
               
                if n%2 == 0:
                    memo[n] = getNums(n//2)
                    
                else:
                    memo[n] = getNums((n-1)//2) + getNums((n+1)//2)
            maximum = max(maximum,memo[n])
            return memo[n]
        
        for i in range(2,n + 1):
            getNums(i)
        
    
        return maximum
