class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()
        
        @cache
        def dp(index, factor):
            if index == len(satisfaction):
                return 0

            takeit = factor*satisfaction[index] + dp(index + 1, factor + 1)
            leaveIt = dp(index + 1, factor)
            return max(takeit, leaveIt)
        
        return dp(0,1)
