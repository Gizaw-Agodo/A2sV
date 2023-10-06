class Solution:
    def knightDialer(self, n: int) -> int:
        grid = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
        dir = [(2,1),(2,-1),(1,2),(-1,2),(-2,-1),(-2,1),(-1,-2),(1,-2)]

        def isBounded (i,j):
            return 0 <= i < 4 and 0<=j <3
        
        @cache
        def dfs (row,col, nums):
            if nums == n:
                return 1
            count = 0
            for i , j in dir : 
                nrow, ncol = row + i , col + j
                if isBounded(nrow, ncol) and grid[nrow][ncol] not  in ["*",'#']:
                    count += dfs(nrow, ncol, nums + 1)
            return count

        answer = 0
        for i in range(4):
            for j in range(3):
                if grid[i][j] not in ["*",'#']:
                    answer += dfs(i, j , 1)

        return answer % 1000000007

            




        
