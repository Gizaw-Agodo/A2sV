class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        pref_sum =[[0] * (n+1) for _ in range(n+1)]
        for row1, col1, row2, col2  in queries:
            pref_sum[row1][col1] += 1
            pref_sum[row1][col2 + 1] += -1    
            pref_sum[row2+1][col1] -= 1
            pref_sum[row2+1][col2 +1] += 1
        
        for i in range(len(pref_sum)):
            for j in range(1,len(pref_sum)):
                pref_sum[i][j] += pref_sum[i][j-1]
                
        for i in range(len(pref_sum)):
            for j in range(1,len(pref_sum)):
                pref_sum[j][i] += pref_sum[j-1][i]
        sliced = [pref_sum[i][0:len(pref_sum)-1] for i in range(len(pref_sum)-1)]
        return sliced
            
        