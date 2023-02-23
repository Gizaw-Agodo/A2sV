class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix   
        self.pref_sum =[[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        
        for rowindex in range(len(self.matrix)):
            for colindex in range(len(self.matrix[0])):
                row_index = rowindex + 1
                col_index = colindex + 1
                self.pref_sum[row_index][col_index] = self.pref_sum[row_index-1][col_index] + self.pref_sum[row_index][col_index-1] - self.pref_sum[row_index-1][col_index-1]+ self.matrix[rowindex][colindex]
              
       
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        range_sum = self.pref_sum[row2+1][col2+1] - self.pref_sum[row2+1][col1] - self.pref_sum[row1][col2+1] + self.pref_sum[row1][col1]
        return range_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)