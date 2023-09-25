class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}
        target = ceil(sum(stones)/2)

        def dp (index, total ):
            if total >= target or index == len(stones):
                return abs(total - (sum(stones) - total))
            
            if ( index, total ) in memo:
                return memo[(index, total)]
            
            take = dp(index + 1, total + stones[index])
            notTake = dp(index + 1, total)
            memo[(index, total )] = min(take, notTake)

            return memo[(index,total)]
        return dp(0, 0)
        

            
