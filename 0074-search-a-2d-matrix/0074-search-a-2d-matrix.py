class Solution:
   
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix[0])
        m = len(matrix)
        high = m*n-1
        low = 0 
        
        return self.search(matrix,low,high,target,n)
          
        
    def search(self,matrix,low,high,target,n) ->bool:
        while high >= low :
            mid_index = (high + low)//2
            row = mid_index//n
            col = mid_index % n
            elem = matrix[row][col]
            if elem == target:
                return True
            elif elem > target:
                return self.search(matrix,low,mid_index-1,target,n)
            else:
                return self.search(matrix,mid_index +1 ,high,target,n)
        else:
            return False