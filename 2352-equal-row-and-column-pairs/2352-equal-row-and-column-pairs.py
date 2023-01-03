class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        answer = 0
        transpose = [[0]*len(grid[0]) for i in range(len(grid))]
        
        
        # finding transpose of the original array
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                transpose[j][i] = grid[i][j]
       
        count = defaultdict(int)
        for i in range(len(transpose)):
            temp = "#".join(map(str,transpose[i]))
            count[temp] +=1
       
        #looping in the original array and comparing with transpose
        for element in grid:
            if element in transpose:
                temp = "#".join(map(str,element))
                answer +=count[temp]
        return answer
                
            
        