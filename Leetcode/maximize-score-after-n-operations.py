class Solution:
    def maxScore(self, nums: List[int]) -> int:

        @cache
        def dp(mask, opperations):
            if opperations == (len(nums)//2) + 1:
                return 0
            
            score = 0
            for i in range(len(nums)):
                if (mask >> i) & 1:
                    continue

                for j in range( i + 1, len(nums)):
                    if (mask >> j)& 1 :
                        continue
                    
                    currMask = (1 << i)| (1 << j) | (mask)
                    s = math.gcd(nums[i],nums[j])*opperations
                    currScore = s + dp(currMask, opperations + 1) 
                    score = max(score, currScore)

            return score
        
        return dp(0, 1)

        
        
