class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pref_sum = [0]*(len(nums) + 1)
        for start,end in requests:
            pref_sum[start] += 1
            pref_sum[end+1] -= 1
            
        for i in range(1,len(pref_sum)):
            pref_sum[i] += pref_sum[i-1]
        
        pref_sum.sort(reverse = True)
        nums.sort(reverse = True)
        
        max_score = 0
        for i in range(len(nums)):
            max_score += pref_sum[i] *nums[i]
            
        return max_score % 1000000007
        
        
        
        
        
        