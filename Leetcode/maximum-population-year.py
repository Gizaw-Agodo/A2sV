class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        total = [0]*2051
        for birth, death in logs:
            total[birth] += 1
            total[death] -= 1
        for i in range(1, len(total)):
            total[i] += total[i-1]
        
        max_val = float('-inf')
        max_index = 0
        for index, val in enumerate(total) : 
            if val > max_val : 
                max_val = val
                max_index = index
        return max_index
