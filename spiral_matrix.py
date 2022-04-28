class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        last_col = len(matrix[0])-1
        last_row = len(matrix)-1
        c,r = 0,0
        response = []
        while c <= last_col and r <= last_row:
            for i in range (c ,last_col+1):
                response.append(matrix[r][i])
            r+=1
            
            for i in range (r,last_row+1):
                response.append(matrix[i][last_col])
            last_col -=1
            
            if r <= last_row:
                for i in range(last_col,c-1,-1):
                    response.append(matrix[last_row][i])
                last_row -=1
            if c <= last_col:
                for i in range(last_row,r-1,-1):
                    response.append(matrix[i][c])
                c+=1
        return response
