class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        if m*n != r*c:
            return mat
        
        new_mat = [[0]*c for _ in range(r)]
        row,col = 0,0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if col < c:
                    new_mat[row][col] = mat[i][j]
                    col += 1
                else:
                    col = 0
                    row +=1
                    new_mat[row][col] = mat[i][j]
                    col += 1
                    
                    
        return new_mat
                    
                