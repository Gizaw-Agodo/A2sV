class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # taking a set of rows and cols to be updated
        row_to_update = set()
        col_to_update = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] ==0:
                    row_to_update.add(i)
                    col_to_update.add(j)
                    
        #iterate through each row and col to be updated and update the value
        for i in row_to_update:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in col_to_update:
            for k in range(len(matrix)):
                matrix[k][j]  = 0
          