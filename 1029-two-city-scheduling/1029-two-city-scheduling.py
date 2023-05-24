class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = [[costs[i][0]- costs[i][1],i] for i in range(len(costs))]
        diff.sort()
        half = len(costs)/2
        answer = 0
        for i in range(len(diff)):
            index = diff[i][1]
            if i < half:
                answer += costs[index][0]
            else:
                answer += costs[index][1]
        return answer
        
        