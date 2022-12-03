class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==2:
            return min(cost[0],cost[1])
        for i in range(2,len(cost)):
            if  i == len(cost)-1:
                cost[i] =  min(cost[i-1],cost[i-2]+cost[i])
            else:
                cost[i] += min(cost[i-1],cost[i-2])
        return cost[-1]