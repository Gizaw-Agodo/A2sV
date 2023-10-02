class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        @cache
        def dp(index , a, b):
            if index == len(costs):
                if a == b:
                    return 0
                return float('inf')

            citya  = costs[index][0] + dp(index + 1, a + 1, b)
            cityb  = costs[index][1] + dp(index + 1 , a , b + 1)
            return min(citya, cityb)
        
        return dp(0,0,0)





        
