class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0]*(n-2) for _ in range(n-2)]
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                maxLocal[i][j] = max(grid[k][l] for k in range(i,i+3) for l in range(j, j+3))
        return maxLocal  