class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon[0])
        n = len(dungeon)
        memo = [[float('inf')] *( m + 1) for _ in range(n + 1)]
        memo[n-1][m-1] = max( 1 +  -1 * dungeon[n-1][m-1] , 1)
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m-1 : 
                    continue
                minimum =  min(memo[i][j + 1],memo[i + 1][j])
                memo[i][j] = max(1,minimum - dungeon[i][j])
        
        return memo[0][0]
