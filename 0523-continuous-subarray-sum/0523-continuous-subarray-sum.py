class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0:-1}
        prefixsum = 0
        '''
        [3,3]
        '''
        for i in range(len(nums)):
            prefixsum += nums[i]
            if prefixsum%k  in dic :
                if i - dic[prefixsum%k] >=2 :
                    return True
            else:
                dic[prefixsum%k] = i
        return False
                
                
            