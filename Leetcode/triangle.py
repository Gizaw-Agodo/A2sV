class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)       
        for i in range(1,n):
            m = len(triangle[i])
            start = 0
            while start < m:
                if start == 0 :
                    triangle[i][start] += triangle[i-1][start]
                elif start == m-1:
                    triangle[i][start] += triangle[i-1][start-1]
                else:                    
                    triangle[i][start] += min(triangle[i-1][start-1],triangle[i-1][start])
                start +=1
        
        return min(triangle[n-1])
        