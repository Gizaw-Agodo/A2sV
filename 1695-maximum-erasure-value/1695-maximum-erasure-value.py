class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        start = 0
        maximum = 0
        prefsum = [0]*len(nums)
        prefsum[0] = nums[0]
        for i in range(len(nums)):
            if i > 0:
                prefsum[i] = nums[i] + prefsum[i-1]
            dic[nums[i]]+=1
           
            while dic[nums[i]] > 1:
                dic[nums[start]] -=1
                start +=1
            maximum = max(maximum,prefsum[i] - prefsum[start] +nums[start] )
        
        return maximum
                
                
                
            